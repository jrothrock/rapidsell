"""Sign in route and handling."""
from __future__ import annotations

import dataclasses
import os

import boto3
from chalice.app import Request


@dataclasses.dataclass
class SignInRequest:
    """The signin request params structure."""

    email: str
    password: str

    @classmethod
    def from_json_body(cls, payload: dict[str, str]) -> SignInRequest:
        """Create the SignInRequest class from the payload."""
        return cls(email=payload["email"], password=payload["password"])


@dataclasses.dataclass
class SignInResponse:
    """The sign in response structure."""

    access_token: str


def user_sign_in(request: Request):
    """User sign in."""
    sign_in_params = SignInRequest.from_json_body(request.json_body)

    boto_client = boto3.client("cognito-idp")
    boto_response = boto_client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        ClientId=os.environ.get("AWS_COGNITO_CLIENT_ID"),
        AuthParameters={
            "USERNAME": sign_in_params.email,
            "PASSWORD": sign_in_params.password,
        },
    )

    access_token = boto_response["AuthenticationResult"]["AccessToken"]
    response = SignInResponse(access_token=access_token)

    return dataclasses.asdict(response)
