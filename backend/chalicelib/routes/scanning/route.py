"""Scanning routes."""
import os

from chalice import Blueprint
from chalice import CognitoUserPoolAuthorizer

from chalicelib.routes.scanning.presign import presign_s3_url


scanning = Blueprint(__name__)

pool_name = os.environ.get("AWS_COGNITO_POOL_NAME")
provider_arn = os.environ.get("AWS_COGNITO_POOL_ARN")
authorizer = CognitoUserPoolAuthorizer(
    pool_name, provider_arns=["${provider_arn}"])

@scanning.route("/scanning/presign", methods=["GET"], authorizer=authorizer, cors=True)
def presign():
    """Get a presigned URL for the s3 scanning bucket."""
    return presign_s3_url(scanning.current_request)

