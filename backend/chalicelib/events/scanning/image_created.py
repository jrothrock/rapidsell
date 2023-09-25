"""Handles the event for the s3 image creation."""
from __future__ import annotations

import datetime
import uuid

import boto3

from chalicelib import _scraping
from chalicelib._dynamo.scanning import ScanningImageModel


def scan_image_created(event):
    """Create a dynamo record for the scanned image to be used for scraping."""
    uuid_for_image = uuid.uuid4()

    s3_client = boto3.client("s3")
    signed_url = s3_client.generate_presigned_url(
        "get_object", Params={"Bucket": event.bucket, "Key": event.key}, ExpiresIn=300
    )

    pk = f"ScanningImage#{uuid_for_image}"
    sk = "ScanningImage#meta"
    scanning_image = ScanningImageModel(
        pk,
        sk,
        signed_url=signed_url,
        image_key=event.key,
        image_bucket=event.bucket,
        ttl=datetime.timedelta(minutes=5),
    )
    scanning_image.save()

    _scraping.run_lens_scraping(uuid_for_image, event.key, event.bucket)
