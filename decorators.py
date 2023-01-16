from functools import wraps
from random import randint
from typing import Callable
from pizza import Pizza


def log(sample: str) -> Callable:
    """Decorator, returns time of function's work"""
    def outer_wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner_wrapper(pizza: Pizza) -> str:
            result = function(pizza)
            size = pizza.size
            time = randint(1, 42)
            print(sample.format(size, time))
            return result
        return inner_wrapper
    return outer_wrapper
