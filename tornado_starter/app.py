from __future__ import annotations

import os
from pathlib import Path
import asyncio

import tornado.ioloop
import tornado.web
import tornado.options
from dotenv import load_dotenv

from .config import settings
from .routes import get_routes
from .db import init_mongo, get_db
from .cache import init_redis, get_redis


BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables as early as possible
load_dotenv(dotenv_path=BASE_DIR / ".env", override=False)


class Application(tornado.web.Application):
    """Tornado application with pre-configured routes and settings."""

    def __init__(self) -> None:
        super().__init__(get_routes(static_path=settings["static_path"]), **settings)
        # Initialize MongoEngine and expose pymongo db for convenience
        init_mongo()
        self.settings["db"] = get_db()
        # Initialize Redis client and store reference
        loop = asyncio.get_event_loop_policy().get_event_loop()
        loop.run_until_complete(init_redis())
        self.settings["redis"] = get_redis()


def make_app() -> Application:
    """Factory to create the Tornado application instance."""

    return Application()


def main() -> None:
    """Entrypoint for running the Tornado server."""

    tornado.options.parse_command_line()

    app = make_app()
    port = int(os.getenv("APP_PORT", 8888))

    print(f"启动Tornado服务器在端口 {port}")
    print(f"访问地址: http://localhost:{port}")

    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

