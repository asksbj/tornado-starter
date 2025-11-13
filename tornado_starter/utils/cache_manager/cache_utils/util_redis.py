import redis
from tornado_starter.config import REDIS_URL


def connect():
    return redis.Redis.from_url(REDIS_URL, decode_responses=True)