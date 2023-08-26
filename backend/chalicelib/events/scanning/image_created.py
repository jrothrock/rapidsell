"""Handles the event for the s3 image creation."""
from __future__ import annotations

import datetime
import os
import uuid

import boto3

from chalicelib import _scraping


def scan_image_created(event):
    """Create a dynamo record for the scanned image to be used for scraping."""
    uuid_for_image = uuid.uuid4()

    ttl = (datetime.datetime.now() + datetime.timedelta(minutes=5)).timestamp()

    s3_client = boto3.client("s3")
    signed_url = s3_client.generate_presigned_url(
        "get_object", Params={"Bucket": event.bucket, "Key": event.key}, ExpiresIn=300
    )

    # TODO: Move dynamo schema to a better location.
    dynamo_client = boto3.client("dynamodb")
    dynamo_client.put_item(
        TableName=os.environ.get("AWS_SCANNING_TABLE_NAME"),
        Item={
            "pk": {
                "S": f"ScanningImage#{uuid_for_image}",
            },
            "sk": {
                "S": "ScanningImage#meta",
            },
            "signed_url": {
                "S": signed_url,
            },
            "image_key": {
                "S": event.key,
            },
            "image_bucket": {"S": event.bucket},
            "ttl": {
                "N": str(ttl),
            },
        },
    )

    _scraping.run_lens_scraping(uuid_for_image, event.key, event.bucket)
