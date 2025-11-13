from __future__ import annotations

import asyncio
from typing import Optional

import redis.asyncio as aioredis  # type: ignore[import]

from .config import REDIS_URL

_redis_client: Optional[aioredis.Redis] = None
_redis_lock = asyncio.Lock()


async def init_redis() -> aioredis.Redis:
    """Create and cache a Redis client (asyncio)."""
    global _redis_client
    if _redis_client is None:
        async with _redis_lock:
            if _redis_client is None:
                _redis_client = aioredis.from_url(
                    REDIS_URL,
                    encoding="utf-8",
                    decode_responses=True,
                )
    return _redis_client


def get_redis() -> aioredis.Redis:
    """Return the cached Redis client; call init_redis() first."""
    if _redis_client is None:
        raise RuntimeError("Redis client not initialized. Call init_redis() during startup.")
    return _redis_client


async def close_redis() -> None:
    """Close the Redis client."""
    global _redis_client
    if _redis_client is not None:
        await _redis_client.close()
        _redis_client = None

