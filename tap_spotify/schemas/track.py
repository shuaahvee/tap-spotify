"""Schema definitions for track objects"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    ArrayType,
    BooleanType,
    CustomType,
    IntegerType,
    StringType,
)

from tap_spotify.schemas.album import AlbumObject
from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.external import ExternalIdObject, ExternalUrlObject
from tap_spotify.schemas.restriction import RestrictionObject as TrackRestrictionObject


class TrackObject(CustomType):
    """https://developer.spotify.com/documentation/web-api/reference/#object-trackobject"""

    schema = PropertiesList(
        Property("album", AlbumObject()),
        Property("artists", ArrayType(ArtistObject())),
        Property("available_markets", ArrayType(StringType)),
        Property("disc_number", IntegerType),
        Property("duration_ms", IntegerType),
        Property("explicit", BooleanType),
        Property("external_ids", ExternalIdObject()),
        Property("external_urls", ExternalUrlObject()),
        Property("href", StringType),
        Property("id", StringType),
        Property("is_local", BooleanType),
        Property("is_playable", BooleanType),
        # Property("linked_from", TrackObject()),
        Property("name", StringType),
        Property("popularity", IntegerType),
        Property("preview_url", StringType),
        Property("restrictions", TrackRestrictionObject()),
        Property("track_number", IntegerType),
        Property("type", StringType),
        Property("uri", StringType),
    ).to_dict()

    def __init__(self):
        super().__init__(self.schema)
