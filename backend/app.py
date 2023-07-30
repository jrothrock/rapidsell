"""Entrypoint to the rapidsell application."""
from __future__ import annotations

from chalice import Chalice

from chalicelib.routes.users.route import users

app = Chalice(app_name="backend")
app.register_blueprint(users)


@app.route("/")
def index():
    """Hello world."""
    return {"hello": "world"}
