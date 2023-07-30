"""User routes."""
from chalice import Blueprint

from chalicelib.routes.users.confirm_signup import user_confirm_signup
from chalicelib.routes.users.signup import user_sign_up

users = Blueprint(__name__)


@users.route("/users/sign_up", methods=["POST"])
def sign_up():
    """Sign up for the user."""
    return user_sign_up(users.current_request)


@users.route("/users/sign_up/confirm", methods=["POST"])
def confirm_sign_up():
    """Confirm the sign up of the user."""
    return user_confirm_signup(users.current_request)
