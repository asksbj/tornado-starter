from __future__ import annotations

import json
from datetime import datetime

from .base import BaseHandler


class ApiHandler(BaseHandler):
    """Basic JSON API handler."""

    def get(self, endpoint: str) -> None:
        if endpoint == "info":
            self.write_json(
                {
                    "message": "Tornado API服务运行正常",
                    "timestamp": datetime.now().isoformat(),
                    "version": "1.0.0",
                }
            )
        elif endpoint == "status":
            self.write_json({"status": "ok", "uptime": "运行中"})
        else:
            self.write_json({"error": f"未知的API端点: {endpoint}"}, 404)

    def post(self, endpoint: str) -> None:
        if endpoint == "echo":
            try:
                data = json.loads(self.request.body)
                self.write_json(
                    {
                        "message": "收到数据",
                        "data": data,
                        "timestamp": datetime.now().isoformat(),
                    }
                )
            except json.JSONDecodeError:
                self.write_json({"error": "无效的JSON数据"}, 400)
        else:
            self.write_json({"error": f"未知的API端点: {endpoint}"}, 404)

    def options(self, endpoint: str) -> None:
        self.set_status(204)
        self.finish()

