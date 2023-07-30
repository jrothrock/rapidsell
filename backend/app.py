"""Entrypoint to the rapidsell application."""
from __future__ import annotations

import os
import dataclasses

import boto3
from chalice import Chalice

app = Chalice(app_name="backend")


@app.route("/")
def index():
    """Hello world."""
    return {"hello": "world"}

@dataclasses.dataclass
class SignUpRequest:
    username: str
    password: str

    @classmethod
    def from_json_body(cls, payload: dict[str, str]) -> SignUpRequest:
        return cls(username=payload["username"], password=payload["password"])

@dataclasses.dataclass
class SignUpResponse:
    UserConfirmed: bool

@app.route("/sign_up", methods=["POST"])
def login():
    """User sign up."""
    sign_up_params = SignUpRequest.from_json_body(app.current_request.json_body)
    
    session = boto3.Session(profile_name='default')
    boto_client = session.client('cognito-idp')
    boto_response = boto_client.sign_up(ClientId=os.environ.get("AWS_COGNITO_CLIENT_ID"), Username=sign_up_params.username, Password=sign_up_params.password)
    
    response = SignUpResponse(UserConfirmed=boto_response["UserConfirmed"])

    return dataclasses.asdict(response)

