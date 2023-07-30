"""Sign up route and handling."""
from __future__ import annotations

import dataclasses

import boto3
from chalice.app import Request


@dataclasses.dataclass
class LogOutRequest:
    """The log out request params structure."""

    AccessToken: str

    @classmethod
    def from_json_body(cls, payload: dict[str, str]) -> LogOutRequest:
        """Create the LogOutRequest class from the payload."""
        return cls(AccessToken=payload["access_token"])


@dataclasses.dataclass
class LogOutResponse:
    """The log out response structure."""

    Success: bool


def user_log_out(request: Request):
    """User log out."""
    log_out_params = LogOutRequest.from_json_body(request.json_body)

    boto_client = boto3.client("cognito-idp")
    boto_client.global_sign_out(AccessToken=log_out_params.AccessToken)

    response = LogOutResponse(Success=True)

    return dataclasses.asdict(response)
