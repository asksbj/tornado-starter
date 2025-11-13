from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

import mongoengine as me  # type: ignore[import]


class User(me.Document):
    """Example user document."""

    name = me.StringField(required=True, max_length=100)
    email = me.EmailField(required=True, unique=True)
    created_at = me.DateTimeField(default=datetime.utcnow)

    meta = {
        "collection": "users",
        "indexes": ["email"],
        "ordering": ["-created_at"],
    }

    def to_dict(self) -> Dict[str, Any]:
        created = self.created_at.isoformat() if self.created_at else None
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "created_at": created,
        }

