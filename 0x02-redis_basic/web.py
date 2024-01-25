#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from functools import wraps
from typing import Callable


client = redis.Redis()


def cache(method: Callable) -> Callable:
    '''
    caches the data
    '''
    @wraps(method)
    def wrapper(url) -> str:
        """
        checks whether a url's is cached
        and tracks how many times get_page is called
        """
        client.incr(f'count:{url}')
        result = client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        client.set(f'count:{url}', 0)
        client.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@cache
def get_page(url) -> str:
    """ Makes a http request to a given endpoint
    """
    response = requests.get(url)
    return response.text
