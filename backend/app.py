"""Entrypoint to the rapidsell application."""
from __future__ import annotations

from chalice import Chalice

from chalicelib.routes.users.route import users
from chalicelib.routes.scanning.route import scanning

app = Chalice(app_name="backend")
app.register_blueprint(users)
app.register_blueprint(scanning)


