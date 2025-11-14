import os
import threading
import redis
import logging

from typing import Any, List, Optional, Dict
from tornado_starter.config import REDIS_URL
from tornado_starter.utils.cache_manager import CacheManager

logger = logging.getLogger(__name__)


class RedisCacheManager(CacheManager):

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, url: Optional[str]=None, **kwargs):
        if cls._instance:
            return cls._instance

        with cls._lock:
            if cls._instance:
                return cls._instance
            
            cls._instance = super(RedisCacheManager, cls).__new__(cls)
            cls._instance._init_reids(url=url)

    def _init_redis(self, url: Optional[str]=None):
        self.url = url

        self.connection_pool = redis.ConnectionPool.from_url(
            self.url if self.url else REDIS_URL,
            decode_responses=True,
            max_connections=int(os.getenv('REDIS_MAX_CONNECTIONS', '20')),
            socket_connect_timeout=5,
            socket_timeout=5,
            retry_on_timeout=True,
            health_check_interval=30,
        )

        self._conn = self.get_client()
        self._test_connection()

    def _test_connection(self):
        try:
            r = self.conn()
            r.ping()
            logger.info(f'Conenct to Redis successfully!')
        except redis.ConnectionError as e:
            logger.exception(f'Failed to connect Redis: {e}')

    def get_client(self) -> redis.Redis:
        return redis.Redis(connection_pool=self.connection_pool)

    def conn(self) -> redis.Redis:
        if self._conn is None:
            self._conn = self.get_client()
        return self._conn

    def _full_key(self, key: str) -> str:
        if self.namespace:
            return f"{self.namespace}:{key}"
        return key

    def _do_load(self, key: str, **kwargs) -> Any:
        r = self.conn()
        return r.get(self._full_key(key))

    def _do_save(self, key: str, value: Any, ttl: Optional[int] = None, **kwargs) -> bool:
        r = self.conn()
        ex = ttl if ttl is not None else self.ttl
        if ex is not None:
            return bool(r.set(self._full_key(key), value, ex=ex))
        return bool(r.set(self._full_key(key), value))

    def _do_evict(self, keys: List[str], **kwargs) -> bool:
        r = self.conn()
        if not keys:
            return True
        full_keys = [self._full_key(k) for k in keys]
        deleted = r.delete(*full_keys)
        return deleted is not None
    