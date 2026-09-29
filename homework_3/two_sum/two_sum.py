"""Задача 1. Two sum"""

import sys


def two_sum(arr: list[int], k: int) -> tuple[int, int] | None:
    seen = {}  # значение -> индекс, где оно встретилось впервые
    for j, x in enumerate(arr):
        i = seen.get(k - x)
        if i is not None:
            return i, j
        # кладем после проверки, чтобы элемент не сложился сам с собой
        seen.setdefault(x, j)
    return None


def parse(text: str) -> tuple[list[int], int]:
    """Массив и k, разделенные '/' или переводом строки"""
    parts = [p for p in text.replace("\n", "/").split("/") if p.strip()]
    if len(parts) != 2:
        raise ValueError("нужны массив и k, разделенные '/'")
    return [int(x) for x in parts[0].split()], int(parts[1])


def solve(text: str) -> str:
    answer = two_sum(*parse(text))
    return "пары нет" if answer is None else f"{answer[0]} {answer[1]}"


def trace(arr: list[int], k: int) -> None:
    print(f"arr = {arr}, k = {k}")
    print()
    head = (
        f"{'шаг':>4} | {'j':>3} | {'arr[j]':>6} | {'ищем k - arr[j]':>15}"
        f" | {'нашли':<12} | seen (значение: индекс)"
    )
    print(head)
    print("-" * len(head))

    seen = {}
    for j, x in enumerate(arr):
        i = seen.get(k - x)
        found = "-" if i is None else f"да, i = {i}"
        if i is None:
            seen.setdefault(x, j)
        print(f"{j + 1:>4} | {j:>3} | {x:>6} | {k - x:>15} | {found:<12} | {seen}")
        if i is not None:
            print(f"\nответ: {i} {j}")
            return
    print("\nпары нет")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(*parse(" ".join(argv[1:]) or "3 8 -1 5 3 12 / 6"))
        return
    print(solve(" ".join(argv) if argv else sys.stdin.read()))


if __name__ == "__main__":
    main(sys.argv[1:])
