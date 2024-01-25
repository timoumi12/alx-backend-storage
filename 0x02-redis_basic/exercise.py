#!/usr/bin/env python3
'''cache class'''
from functools import wraps
import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    '''Writing strings to Redis'''

    def __init__(self) -> None:
        '''creates redis instance, flushes the instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        '''generate a random key, store the input data, return key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Optional[callable] = None) -> any:
        '''take a string key argurment'''
        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key):
        '''Retrieve a string value from a Redis data storage'''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key):
        '''Retrieve an integer value from a Redis data storage'''
        return self.get(key, lambda x: int(x))
