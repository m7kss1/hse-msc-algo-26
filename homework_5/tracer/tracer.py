"""Задача 1. Трассировка рекурсивных вызовов"""

from contextvars import ContextVar
from functools import wraps

# глубина общая для вложенных декорированных функций, но своя в каждом контексте
_depth = ContextVar("trace_depth", default=0)


def tracer(func):
    """Печатать вход, результат и исключение с отступом по глубине"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        depth = _depth.get()
        indent = "  " * depth
        arguments = [repr(arg) for arg in args]
        arguments += [f"{key}={value!r}" for key, value in kwargs.items()]
        print(f"{indent}-> {func.__name__}({', '.join(arguments)})")
        token = _depth.set(depth + 1)  # вложенный вызов получит больший отступ
        try:
            result = func(*args, **kwargs)
        except BaseException as error:
            print(f"{indent}!! {func.__name__}: {type(error).__name__}: {error}")
            raise
        else:
            print(f"{indent}<- {func.__name__} = {result!r}")
            return result
        finally:
            _depth.reset(token)  # и при возврате, и при исключении
    return wrapper


@tracer
def factorial(n):
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    return 1 if n <= 1 else n * factorial(n - 1)


if __name__ == "__main__":
    factorial(4)
