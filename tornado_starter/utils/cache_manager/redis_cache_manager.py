from typing import Any, List, Optional
import redis  # type: ignore[import]
from tornado_starter.config import REDIS_URL
from tornado_starter.utils.cache_manager import CacheManager
from tornado_starter.utils.cache_manager.cache_utils.util_redis import connect as redis_conn


class RedisCacheManager(CacheManager):

    def _full_key(self, key: str) -> str:
        if self.namespace:
            return f"{self.namespace}:{key}"
        return key

    def conn(self):
        if self._conn is None:
            self._conn = redis_conn()
        return self._conn

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
    