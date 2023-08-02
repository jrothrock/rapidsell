"""Will create presigned urls for the frontend to upload photos to."""
from __future__ import annotations

import dataclasses
import datetime
import os

import boto3
from chalice.app import Request

@dataclasses.dataclass
class PresignResponse:
    """The values for the presigned response."""

    url: str

def presign_s3_url(request: Request):
    """Create a presigned s3 bucket URL."""
    access_token = request.headers.get("Authorization")

    boto_cognito_client = boto3.client("cognito-idp")
    user_response = boto_cognito_client.get_user(AccessToken=access_token)
    user_name = user_response["Username"]

    boto_s3_client = boto3.client('s3')
    bucket = os.environ.get("AWS_SCANNING_BUCKET_NAME")
    time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    key = f"{user_name}/{time}.png"
    s3_response = boto_s3_client.generate_presigned_url('put_object',
                                                    Params={'Bucket': bucket, 'Key': key},
                                                    ExpiresIn=3600)

    print(s3_response)
    response = PresignResponse(url=s3_response)
    return dataclasses.asdict(response)