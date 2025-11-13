#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""应用启动脚本."""

import os

from tornado_starter.app import main


def bootstrap_environment() -> None:
    os.environ.setdefault("APP_PORT", "8888")
    os.environ.setdefault("APP_DEBUG", "True")


if __name__ == "__main__":
    bootstrap_environment()
    main()

