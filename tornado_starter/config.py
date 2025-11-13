from __future__ import annotations

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_PATH = BASE_DIR / "templates"
STATIC_PATH = BASE_DIR / "static"

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "tornado_starter")

settings = {
    "debug": os.getenv("APP_DEBUG", "True").lower() == "true",
    "template_path": str(TEMPLATE_PATH),
    "static_path": str(STATIC_PATH),
    "cookie_secret": os.getenv("SECRET_KEY", "your-secret-key-change-this"),
    "xsrf_cookies": True,
    "login_url": "/login",
    "autoescape": "xhtml_escape",
}

__all__ = ["BASE_DIR", "settings", "MONGODB_URI", "MONGODB_DB"]

