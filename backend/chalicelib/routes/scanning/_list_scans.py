"""List scans route and handling."""
from __future__ import annotations

import dataclasses

import boto3
from botocore.config import Config
from chalice.app import Request

from chalicelib._dynamo.scanning import ScannedImageModel


@dataclasses.dataclass
class ListScansRequest:
    """The list scans request params structure."""

    email: str
    password: str

    @classmethod
    def from_json_body(cls, payload: dict[str, str]) -> ListScansRequest:
        """Create the ListScansRequest class from the payload."""
        return cls(email=payload["email"], password=payload["password"])


@dataclasses.dataclass
class ScanResponse:
    """The response for a ScannedImageModel."""

    # A presigned S3 URL to access the image.
    imageUrl: str
    serpFoundTitle: str
    serpFoundPrice: float
    serpJsonResponse: str


@dataclasses.dataclass
class ListScansResponse:
    """The list scans response structure."""

    scans: list[ScanResponse]


def _create_scan_response_item_from_results(item: ScannedImageModel) -> ScanResponse:
    """Transform ScannedImage dynamo record to Scan response."""
    boto_s3_client = boto3.client("s3", config=Config(signature_version="s3v4"))
    s3_response = boto_s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": item.image_bucket, "Key": item.image_key},
        ExpiresIn=3600,
    )

    return ScanResponse(
        imageUrl=s3_response,
        serpFoundTitle=item.serp_found_title,
        serpFoundPrice=item.serp_found_price,
        serpJsonResponse=item.serp_json_response,
    )


def list_scans_for_user(request: Request):
    """Will return a list of the scanned images for the user."""
    access_token = request.headers.get("X-ACCESS-TOKEN")

    boto_cognito_client = boto3.client("cognito-idp")
    user_response = boto_cognito_client.get_user(AccessToken=access_token)
    user_name = user_response["Username"]

    results = ScannedImageModel.inverted_index.query(
        "ScannedImage#meta",
        ScannedImageModel.pk.startswith(f"ScannedImage#{user_name}#"),
    )
    scan_items = [_create_scan_response_item_from_results(item) for item in results]

    response = ListScansResponse(scans=scan_items)

    return dataclasses.asdict(response)
