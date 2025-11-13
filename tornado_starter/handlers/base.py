from __future__ import annotations

import json

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """Common behaviour for all request handlers."""

    def set_default_headers(self) -> None:
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def write_json(self, data: dict, status_code: int = 200) -> None:
        self.set_status(status_code)
        self.write(json.dumps(data, ensure_ascii=False, indent=2))

    def get_current_user(self) -> bytes | None:
        return self.get_secure_cookie("user")

