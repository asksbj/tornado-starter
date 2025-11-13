from __future__ import annotations

import json

import mongoengine as me  # type: ignore[import]

from .base import BaseHandler
from ..models import User


class UserHandler(BaseHandler):
    """Simple CRUD-style handler backed by MongoEngine."""

    def get(self) -> None:
        """Return a list of users."""
        try:
            limit = int(self.get_argument("limit", "20"))
        except ValueError:
            self.write_json({"error": "limit must be an integer"}, 400)
            return

        limit = max(1, min(limit, 100))
        users = list(User.objects.limit(limit))
        self.write_json(
            {
                "count": len(users),
                "items": [user.to_dict() for user in users],
            }
        )

    def post(self) -> None:
        """Create a new user."""
        try:
            payload = json.loads(self.request.body or "{}")
        except json.JSONDecodeError:
            self.write_json({"error": "Invalid JSON payload"}, 400)
            return

        name = (payload.get("name") or "").strip()
        email = (payload.get("email") or "").strip()

        if not name or not email:
            self.write_json({"error": "name and email are required"}, 400)
            return

        user = User(name=name, email=email)
        try:
            user.save()
        except (me.ValidationError, me.NotUniqueError) as exc:
            self.write_json({"error": str(exc)}, 400)
            return

        self.write_json({"item": user.to_dict()}, 201)

