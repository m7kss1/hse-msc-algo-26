"""Задача 1. Палиндром"""

import sys


def is_palindrome(n: int) -> bool:
    """Читается ли положительное число одинаково слева направо и справа налево"""
    x, rev = n, 0
    while x > 0:
        rev = rev * 10 + x % 10  # приклеили последнюю цифру x к rev
        x //= 10  # и отрезали её от x
    return rev == n


def trace(n: int) -> None:
    """Печатает пошаговую таблицу состояний цикла"""
    x, rev = n, 0
    print(f"{'шаг':>4} | {'цифра':>5} | {'x (остаток)':>11} | {'rev':>8}")
    print("-" * 40)
    print(f"{0:>4} | {'-':>5} | {x:>11} | {rev:>8}")
    step = 0
    while x > 0:
        step += 1
        d = x % 10
        rev, x = rev * 10 + d, x // 10
        print(f"{step:>4} | {d:>5} | {x:>11} | {rev:>8}")
    print(f"\nrev = {rev}, n = {n}  ->  {rev == n}")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(int(argv[1]) if len(argv) > 1 else 12321)
        return
    print(is_palindrome(int(argv[0] if argv else sys.stdin.read())))


if __name__ == "__main__":
    main(sys.argv[1:])
