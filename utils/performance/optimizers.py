import time
from functools import wraps
from typing import Callable, Any

def async_timed_cache(ttl: int = 300):
    def decorator(func: Callable):
        cache = {}
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache and time.time() - cache[key]['time'] < ttl:
                return cache[key]['value']
            result = await func(*args, **kwargs)
            cache[key] = {'value': result, 'time': time.time()}
            return result
        return wrapper
    return decorator
