"""Задача 1. Построение minheap за O(N log N) и за O(N)"""

import random
import sys
from time import perf_counter


def sift_up(arr: list, i: int) -> None:
    """Поднимать arr[i], пока он меньше родителя"""
    while i > 0:
        parent = (i - 1) // 2
        if arr[parent] <= arr[i]:
            return
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def sift_down(arr: list, i: int, n: int) -> None:
    """Опускать arr[i] внутри arr[:n], пока он больше меньшего из детей"""
    while True:
        smallest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            return
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def makeheap_n_log_n(arr: list) -> None:
    """Добавлять элементы по одному и поднимать каждый, O(N log N)"""
    for i in range(1, len(arr)):
        sift_up(arr, i)  # arr[:i] уже куча


def makeheap(arr: list) -> None:
    """Опускать внутренние узлы от последнего к корню, O(N)"""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)  # поддеревья детей i уже кучи


def is_min_heap(arr: list) -> bool:
    return all(arr[(i - 1) // 2] <= arr[i] for i in range(1, len(arr)))


class SwapCounter(list):
    """Список, который считает записи по индексу, один обмен дает две записи"""

    def __init__(self, items):
        super().__init__(items)
        self.writes = 0

    def __setitem__(self, index, value):
        self.writes += 1
        super().__setitem__(index, value)


def count_swaps(build, nums: list) -> int:
    arr = SwapCounter(nums)
    build(arr)
    return arr.writes // 2


def trace(nums: list) -> None:
    print(f"nums = {nums}")
    steps = [
        ("makeheap_n_log_n: добавляем arr[i] и поднимаем", range(1, len(nums)), sift_up),
        ("makeheap: опускаем внутренние узлы с конца", range(len(nums) // 2 - 1, -1, -1),
         lambda arr, i: sift_down(arr, i, len(arr))),
    ]
    width = max(len(str(nums)), len("массив после шага"))  # у перестановок одна длина строки
    for title, indexes, sift in steps:
        print(f"\n{title}")
        print(f"  {'i':>2} | элемент | {'массив после шага':<{width}} | обменов")
        arr = SwapCounter(nums)
        for i in indexes:
            before, value = arr.writes, arr[i]
            sift(arr, i)
            print(f"  {i:>2} | {value:>7} | {str(list(arr)):<{width}} | {(arr.writes - before) // 2}")
        print(f"  всего обменов {arr.writes // 2}")


def measure(build, nums: list, repeat: int = 3) -> float:
    """Лучшее из repeat время построения кучи на копии nums"""
    best = float("inf")
    for _ in range(repeat):
        arr = nums.copy()
        start = perf_counter()
        build(arr)
        best = min(best, perf_counter() - start)
        assert is_min_heap(arr)
    return best


def benchmark(sizes: list[int]) -> None:
    rng = random.Random(42)
    print(f"{'массив':<14} {'n':>9} | {'время, с':^21} | {'обмены':^21}")
    print(f"{'':<14} {'':>9} | {'N log N':>10} {'N':>10} | {'N log N':>10} {'N':>10}")
    for n in sizes:
        cases = [
            ("случайный", [rng.randrange(n) for _ in range(n)]),
            ("по убыванию", list(range(n, 0, -1))),
            ("по возрастанию", list(range(n))),
        ]
        for name, nums in cases:
            times = [measure(build, nums) for build in (makeheap_n_log_n, makeheap)]
            swaps = [count_swaps(build, nums) for build in (makeheap_n_log_n, makeheap)]
            print(f"{name:<14} {n:>9} | {times[0]:>10.4f} {times[1]:>10.4f} | {swaps[0]:>10} {swaps[1]:>10}")


def parse(text: str) -> list[int]:
    for ch in "[],":
        text = text.replace(ch, " ")
    return [int(x) for x in text.split()]


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(parse(" ".join(argv[1:])) if len(argv) > 1 else [7, 6, 5, 4, 3, 2, 1])
    elif argv and argv[0] == "--bench":
        benchmark([int(x) for x in argv[1:]] or [10_000, 100_000, 1_000_000])
    else:
        nums = parse(" ".join(argv) if argv else sys.stdin.read())
        for build in (makeheap_n_log_n, makeheap):
            arr = nums.copy()
            build(arr)
            print(arr)


if __name__ == "__main__":
    main(sys.argv[1:])
