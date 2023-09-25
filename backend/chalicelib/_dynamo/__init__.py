"""Holds the dynamo tables and models."""
from pynamodb.attributes import UnicodeAttribute
from pynamodb.indexes import AllProjection
from pynamodb.indexes import GlobalSecondaryIndex


class InvertedIndex(GlobalSecondaryIndex):
    """This class represents the inverted secondary index."""

    class Meta:
        """Meta information in relation to the inverted index."""

        index_name = "InvertedIndex"
        # All attributes are projected
        projection = AllProjection()

    sk = UnicodeAttribute(hash_key=True)
    pk = UnicodeAttribute(range_key=True)
