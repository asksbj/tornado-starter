from typing import List, Optional, Any
from abc import ABC, abstractmethod

class CacheManager(ABC):

    def __init__(
        self, 
        namespace: Optional[str] = None,
        ttl: Optional[int] = None,
        conn: Optional[Any] = None):
        self.namespace = namespace
        self.ttl = ttl
        self._conn = conn

    @abstractmethod
    def conn(self):
        pass

    def reset_conn(self):
        self._conn = None

    def check_available(self) -> bool:
        return self.conn() is not None

    @abstractmethod
    def _do_load(self, key: str, **kwargs) -> Any:
        pass

    def load(self, key: str, **kwargs) -> Any:
        return self._do_load(key, **kwargs)

    @abstractmethod
    def _do_save(self, key: str, value: Any, ttl: Optional[int]=None, **kwargs) -> bool:
        pass

    def save(self, key: str, value: Any, ttl: Optional[int]=None, **kwargs) -> bool:
        return self._do_save(key, value, ttl, **kwargs)

    @abstractmethod
    def _do_evict(self, keys: List[str], **kwargs) -> bool:
        pass

    def evict(self, keys: List[str], **kwargs) -> bool:
        return self._do_evict(keys, **kwargs)


    