from __future__ import annotations

from datetime import datetime

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """Render landing page."""

    def get(self) -> None:
        self.render(
            "index.html",
            title="Tornado Web应用",
            message="欢迎使用Tornado框架！",
            current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )

