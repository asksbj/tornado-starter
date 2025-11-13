from __future__ import annotations

from typing import Optional

from mongoengine import connect, disconnect  # type: ignore[import]
from mongoengine.connection import get_db as _get_db  # type: ignore[import]

from .config import MONGODB_DB, MONGODB_URI

_connected: bool = False


def init_mongo(alias: str = "default") -> None:
    """Initialize MongoEngine connection once."""
    global _connected
    if _connected:
        return
    connect(
        db=MONGODB_DB,
        host=MONGODB_URI,
        alias=alias,
        uuidRepresentation="standard",
    )
    _connected = True


def get_db():
    """Return underlying PyMongo database from MongoEngine."""
    return _get_db()


def close_mongo(alias: str = "default") -> None:
    """Close MongoEngine connection."""
    global _connected
    if _connected:
        disconnect(alias=alias)
        _connected = False


