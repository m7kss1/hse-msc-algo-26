"""Задача 3. Простые числа"""

import sys


def count_primes(n: int) -> int:
    """Количество простых чисел, меньших n"""
    if n < 3:  # меньше 3 простых нет вообще
        return 0

    sieve = [True] * n
    sieve[0] = sieve[1] = False

    p = 2
    while p * p < n:
        if sieve[p]:
            for multiple in range(p * p, n, p):
                sieve[multiple] = False
        p += 1

    return sum(sieve)


def trace(n: int) -> None:
    """Печатает состояние решета после каждого вычеркивания"""
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    def show(label: str) -> None:
        print(
            f"{label:<24}"
            + " ".join(f"{i:>2}" if sieve[i] else " ." for i in range(2, n))
        )

    show(f"старт (2..{n - 1}):")
    p = 2
    while p * p < n:
        if sieve[p]:
            for multiple in range(p * p, n, p):
                sieve[multiple] = False
            show(f"вычеркнули кратные {p}:")
        p += 1
    print(f"\nосталось простых: {sum(sieve)}")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(int(argv[1]) if len(argv) > 1 else 30)
        return
    print(count_primes(int(argv[0] if argv else sys.stdin.read())))


if __name__ == "__main__":
    main(sys.argv[1:])
