"""Confirm sign up route and handling."""
from __future__ import annotations

import dataclasses
import os

import boto3
from chalice.app import Request


@dataclasses.dataclass
class ConfirmSignUpRequest:
    """The confirm signup request params structure."""

    username: str
    confirmation_code: str

    @classmethod
    def from_json_body(cls, payload: dict[str, str]) -> ConfirmSignUpRequest:
        """Create the ConfirmSignUpRequest class from the payload."""
        return cls(
            username=payload["username"], confirmation_code=payload["confirmation_code"]
        )


@dataclasses.dataclass
class ConfirmSignUpResponse:
    """The signup response structure."""

    Success: bool


def user_confirm_signup(request: Request):
    """User sign up."""
    sign_up_params = ConfirmSignUpRequest.from_json_body(request.json_body)

    boto_client = boto3.client("cognito-idp")
    boto_client.confirm_sign_up(
        ClientId=os.environ.get("AWS_COGNITO_CLIENT_ID"),
        Username=sign_up_params.username,
        ConfirmationCode=sign_up_params.confirmation_code,
    )

    response = ConfirmSignUpResponse(Success=True)

    return dataclasses.asdict(response)
