"""Задача 3. Сортировка кучей"""

import random
import sys
from time import perf_counter


def sift_down(arr: list, i: int, n: int) -> None:
    """Опускать arr[i] в maxheap arr[:n], пока он меньше большего из детей"""
    while True:
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            return
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def build_max_heap(arr: list) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)


def heapsort(arr: list) -> None:
    """Отсортировать arr по возрастанию на месте"""
    build_max_heap(arr)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # максимум кучи встает на свое место
        sift_down(arr, 0, end)  # куча теперь arr[:end]


# mergesort из homework_6/compare, для сравнения времени
def merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(nums: list) -> list:
    if len(nums) <= 1:
        return nums.copy()
    middle = len(nums) // 2
    return merge(mergesort(nums[:middle]), mergesort(nums[middle:]))


def trace(nums: list) -> None:
    arr = nums.copy()
    n = len(arr)
    print(f"nums = {nums}")
    print("\nстроим maxheap, опускаем внутренние узлы с конца")
    for i in range(n // 2 - 1, -1, -1):
        value = arr[i]
        sift_down(arr, i, n)
        print(f"  i = {i}, элемент {value}: {arr}")
    print(f"maxheap: {arr}\n")
    width = max(len(str(arr[1:])), len("куча"))  # куча после первого шага без максимума
    print(f" шаг | максимум | {'куча':<{width}} | отсортировано")
    for step, end in enumerate(range(n - 1, 0, -1), 1):
        top = arr[0]
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end)
        print(f"{step:>4} | {top:>8} | {str(arr[:end]):<{width}} | {arr[end:]}")
    print(f"\nответ: {arr}")


def measure(sort, nums: list, repeat: int = 3) -> float:
    """Лучшее из repeat время сортировки копии nums"""
    best = float("inf")
    for _ in range(repeat):
        arr = nums.copy()
        start = perf_counter()
        result = sort(arr)
        best = min(best, perf_counter() - start)
        assert (arr if result is None else result) == sorted(nums)
    return best


def benchmark(sizes: list[int]) -> None:
    rng = random.Random(42)
    sorts = [("heapsort", heapsort), ("mergesort", mergesort), ("sorted", sorted)]
    print(f"{'массив':<14} {'n':>7} | " + " ".join(f"{name:>10}" for name, _ in sorts)
          + " | heap/merge heap/sorted")
    for n in sizes:
        cases = [
            ("случайный", [rng.randrange(10**9) for _ in range(n)]),
            ("по возрастанию", list(range(n))),
            ("по убыванию", list(range(n, 0, -1))),
            ("10 значений", [rng.randrange(10) for _ in range(n)]),
        ]
        for name, nums in cases:
            times = [measure(sort, nums) for _, sort in sorts]
            print(f"{name:<14} {n:>7} | " + " ".join(f"{t:>10.4f}" for t in times)
                  + f" | {times[0] / times[1]:>10.1f} {times[0] / times[2]:>11.0f}")


def parse(text: str) -> list[int]:
    for ch in "[],":
        text = text.replace(ch, " ")
    return [int(x) for x in text.split()]


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(parse(" ".join(argv[1:])) if len(argv) > 1 else [5, 2, 9, 1, 7, 3, 8])
    elif argv and argv[0] == "--bench":
        benchmark([int(x) for x in argv[1:]] or [1_000, 10_000, 100_000])
    else:
        nums = parse(" ".join(argv) if argv else sys.stdin.read())
        heapsort(nums)
        print(nums)


if __name__ == "__main__":
    main(sys.argv[1:])
