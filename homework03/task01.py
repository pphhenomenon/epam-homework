from typing import Callable


def cache(times) -> Callable:
    def actual_decorator(function: Callable) -> Callable:
        storage = {}

        def wrapper(*args, **kwargs):
            key = "{} {}".format(args, kwargs)

            if key in storage:
                if storage[key][1] < times:
                    storage[key][1] += 1
                else:
                    storage[key] = [function(*args, **kwargs), 0]
            else:
                storage[key] = [function(*args, **kwargs), 0]

            return storage[key][0]

        return wrapper
    return actual_decorator
