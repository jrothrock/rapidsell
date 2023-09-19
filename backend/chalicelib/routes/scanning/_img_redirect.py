"""Due to Google lens not working with presigned urls, we need to redirect."""
import os

import boto3
from chalice.app import Request
from chalice.app import Response


def img_redirect_s3(request: Request, img_uuid: str):
    """Get the redirect image for google lens."""
    dynamo_client = boto3.client("dynamodb")

    response = dynamo_client.get_item(
        TableName=os.environ.get("AWS_SCANNING_TABLE_NAME"),
        Key={
            "pk": {"S": f"ScanningImage#{img_uuid}"},
            "sk": {"S": "ScanningImage#meta"},
        },
    )

    item = response["Item"]

    return Response(
        body="", headers={"Location": item["signed_url"]["S"]}, status_code=301
    )
