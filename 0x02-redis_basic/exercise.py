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
