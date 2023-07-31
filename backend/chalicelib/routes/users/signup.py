"""Sign up route and handling."""
from __future__ import annotations

import dataclasses
import os

import boto3
from chalice.app import Request


@dataclasses.dataclass
class SignUpRequest:
    """The signup request params structure."""

    email: str
    password: str

    @classmethod
    def from_json_body(cls, payload: dict[str, str]) -> SignUpRequest:
        """Create the SignUpRequest class from the payload."""
        return cls(email=payload["email"], password=payload["password"])


@dataclasses.dataclass
class SignUpResponse:
    """The signup response structure."""

    success: bool


def user_sign_up(request: Request):
    """User sign up."""
    sign_up_params = SignUpRequest.from_json_body(request.json_body)

    boto_client = boto3.client("cognito-idp")
    boto_client.sign_up(
        ClientId=os.environ.get("AWS_COGNITO_CLIENT_ID"),
        Username=sign_up_params.email,
        Password=sign_up_params.password,
    )

    response = SignUpResponse(success=True)

    return dataclasses.asdict(response)
