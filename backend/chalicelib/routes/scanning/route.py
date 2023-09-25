"""Scanning routes."""
import os

from chalice import Blueprint
from chalice import CognitoUserPoolAuthorizer
from chalice import CORSConfig

from chalicelib.routes.scanning._img_redirect import img_redirect_s3
from chalicelib.routes.scanning._list_scans import ListScansResponse
from chalicelib.routes.scanning._list_scans import list_scans_for_user
from chalicelib.routes.scanning._presign import PresignResponse
from chalicelib.routes.scanning._presign import presign_s3_url

scanning = Blueprint(__name__)

pool_name = os.environ.get("AWS_COGNITO_POOL_NAME")
provider_arn = os.environ.get("AWS_COGNITO_POOL_ARN")
authorizer = CognitoUserPoolAuthorizer(pool_name, provider_arns=[f"{provider_arn}"])

cors_config = CORSConfig(
    allow_origin="*",
    allow_headers=["X-ACCESS-TOKEN", "Authorization", "X-MIME-TYPE"],
    max_age=600,
    expose_headers=["X-ACCESS-TOKEN"],
    allow_credentials=True,
)


@scanning.route(
    "/scanning/presign", methods=["GET"], authorizer=authorizer, cors=cors_config
)
def presign() -> PresignResponse:
    """Get a presigned URL for the s3 scanning bucket."""
    return presign_s3_url(scanning.current_request)


@scanning.route("/scanning/img/{img}")
def img_redirect(img: str):
    """Create a 301 redirect for Google lens to access the image."""
    return img_redirect_s3(scanning.current_request, img)


@scanning.route(
    "/scanning/list", methods=["GET"], authorizer=authorizer, cors=cors_config
)
def list_scans() -> ListScansResponse:
    """Get a list of completed scans for the user."""
    return list_scans_for_user(scanning.current_request)
