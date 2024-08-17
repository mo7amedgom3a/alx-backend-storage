#!/usr/bin/env python3
"""0. Create a Cache class. In the __init__ method, store an instance of
the Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.
"""
import redis
import uuid
from typing import Union, Optional, Callable

class Cache:
    """create a Cache class"""


    def __init__(self):
        """initialize a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key, store the input data in Redis using the key
        and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key