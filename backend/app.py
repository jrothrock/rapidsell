"""Entrypoint to the rapidsell application."""
from __future__ import annotations

import os

from chalice import Chalice

# Event Imports
from chalicelib.events.scanning.image_created import scan_image_created
from chalicelib.routes.scanning.route import scanning

# Route Imports
from chalicelib.routes.users.route import users

app = Chalice(app_name="backend")

#######
### ROUTES
#######

app.register_blueprint(users)
app.register_blueprint(scanning)

#######
### EVENTS
#######


# Blueprints don't work for events.
@app.on_s3_event(
    bucket=os.environ.get("AWS_SCANNING_BUCKET_NAME"), events=["s3:ObjectCreated:*"]
)
def scan_img_created(event):
    scan_image_created(event)
