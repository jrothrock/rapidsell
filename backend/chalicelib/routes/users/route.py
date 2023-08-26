"""User routes."""
from chalice import Blueprint

from chalicelib.routes.users.log_out import LogOutResponse
from chalicelib.routes.users.log_out import user_log_out
from chalicelib.routes.users.sign_in import SignInResponse
from chalicelib.routes.users.sign_in import user_sign_in
from chalicelib.routes.users.sign_up import SignUpResponse
from chalicelib.routes.users.sign_up import user_sign_up
from chalicelib.routes.users.sign_up_confirm import ConfirmSignUpResponse
from chalicelib.routes.users.sign_up_confirm import user_confirm_signup

users = Blueprint(__name__)


@users.route("/users/sign_up", methods=["POST"], cors=True)
def sign_up() -> SignUpResponse:
    """Sign up for the user."""
    return user_sign_up(users.current_request)


@users.route("/users/sign_up/confirm", methods=["POST"], cors=True)
def confirm_sign_up() -> ConfirmSignUpResponse:
    """Confirm the sign up of the user."""
    return user_confirm_signup(users.current_request)


@users.route("/users/sign_in", methods=["POST"], cors=True)
def sign_in() -> SignInResponse:
    """Sign in the user."""
    return user_sign_in(users.current_request)


@users.route("/users/log_out", methods=["POST"], cors=True)
def log_out() -> LogOutResponse:
    """Log out the user."""
    return user_log_out(users.current_request)
