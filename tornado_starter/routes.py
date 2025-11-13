from __future__ import annotations

from typing import Iterable

import tornado.web

from .handlers import ApiHandler, MainHandler

def get_routes(static_path: str | None = None) -> Iterable[tuple]:
    """Return the list of route specifications for the application."""

    routes: list[tuple] = [
        (r"/", MainHandler),
        (r"/api/(.*)", ApiHandler),
    ]

    if static_path:
        routes.append(
            (
                r"/static/(.*)",
                tornado.web.StaticFileHandler,
                {"path": static_path},
            )
        )

    return routes

