from functools import wraps
from random import randint
from typing import Callable


def log(sample: str) -> Callable:
    """Decorator, returns time of function's work"""
    def outer_wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner_wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            time = randint(1, 42)
            print(sample.format(time))
            return result
        return inner_wrapper
    return outer_wrapper
