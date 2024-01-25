#!/usr/bin/env python3
'''cache class'''
from functools import wraps
import redis
import uuid
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    '''
    Tracks the number of calls made to a method in a Cache class.
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> any:
        '''Invokes the given method after incrementing its call counter.
        '''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    Store the history of inputs and outputs for a particular function
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> any:
        ''' Invokes the given function after appending its input
        to list called input and its output to a list called output
        '''
        input_list = '{}:inputs'.format(method.__qualname__)
        output_list = '{}:outputs'.format(method.__qualname__)
        self._redis.rpush(input_list, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list, output)
        return output
    return wrapper


class Cache:
    '''Writing strings to Redis'''

    def __init__(self) -> None:
        '''creates redis instance, flushes the instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
