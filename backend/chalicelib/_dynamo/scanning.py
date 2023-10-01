"""Contains the Dynamo models related to scanning."""
# See terraform/modules/backend/scanning/dynamo/main.tf
import os

from pynamodb.attributes import DiscriminatorAttribute
from pynamodb.attributes import NumberAttribute
from pynamodb.attributes import TTLAttribute
from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

from chalicelib._dynamo import InvertedIndex


class ScanModel(Model):
    """Base class for the scanning models."""

    class Meta:
        """Meta information about the scanning models."""

        table_name = os.environ.get("AWS_SCANNING_TABLE_NAME")
        region = "us-west-2"

    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    ttl = TTLAttribute(null=True)
    inverted_index = InvertedIndex()
    cls = DiscriminatorAttribute()


class ScanningImageModel(ScanModel, discriminator="Scanning"):  # type: ignore
    """The model for records that need to be scanned."""

    signed_url = UnicodeAttribute()
    image_key = UnicodeAttribute()
    image_bucket = UnicodeAttribute()


class ScannedImageModel(ScanModel, discriminator="Scanned"):  # type: ignore
    """The model for records that have completed the scanned."""

    image_key = UnicodeAttribute()
    image_bucket = UnicodeAttribute()
    serp_found_title = UnicodeAttribute()
    serp_found_price = NumberAttribute(null=True)
    serp_json_response = UnicodeAttribute()
