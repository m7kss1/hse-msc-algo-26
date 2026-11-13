"""Задача 1. Рекурсивные сортировки и сравнение времени"""

import random
import sys
from functools import wraps
from time import perf_counter


def timer(func):
    """Напечатать время вызова и вернуть результат функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            print(f"{func.__name__}: {elapsed:.6f} с")
    return wrapper


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
    left = mergesort(nums[:middle])
    right = mergesort(nums[middle:])
    return merge(left, right)


def quicksort(nums: list) -> list:
    if len(nums) <= 1:
        return nums.copy()
    pivot = nums[-1]  # на отсортированном массиве получаем худший случай
    less, equal, greater = [], [], []
    for value in nums:
        if value < pivot:
            less.append(value)
        elif value > pivot:
            greater.append(value)
        else:
            equal.append(value)
    return quicksort(less) + equal + quicksort(greater)


def trace(nums: list) -> None:
    print(f"nums = {nums}")
    print("\nmergesort: делим до одного элемента, затем сливаем")

    def show_merge(arr, depth=0):
        indent = "  " * depth
        print(f"{indent}делим {arr}")
        if len(arr) <= 1:
            return arr.copy()
        middle = len(arr) // 2
        left = show_merge(arr[:middle], depth + 1)
        right = show_merge(arr[middle:], depth + 1)
        result = merge(left, right)
        print(f"{indent}{left} + {right} = {result}")
        return result

    def show_quick(arr, depth=0):
        indent = "  " * depth
        if len(arr) <= 1:
            print(f"{indent}{arr}")
            return arr.copy()
        pivot = arr[-1]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        print(f"{indent}опорный {pivot}: {less} | {equal} | {greater}")
        result = show_quick(less, depth + 1) + equal + show_quick(greater, depth + 1)
        print(f"{indent}собираем {result}")
        return result

    show_merge(nums)
    print("\nquicksort: меньше | равно | больше опорного")
    show_quick(nums)


def benchmark(n: int = 600) -> None:
    rng = random.Random(42)
    cases = [
        ("случайные", rng.sample(range(n * 10), n)),
        ("по возрастанию", list(range(n))),
        ("одинаковые", [1] * n),
    ]
    for name, nums in cases:
        print(f"\n{name}, n = {n}")
        for func in (mergesort, quicksort):
            result = timer(func)(nums)
            assert result == sorted(nums)


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace([int(x) for x in argv[1:]] if len(argv) > 1 else [4, 1, 3, 2, 3])
    elif argv and argv[0] == "--bench":
        benchmark(int(argv[1]) if len(argv) > 1 else 600)
    else:
        nums = [int(x) for x in (" ".join(argv) if argv else sys.stdin.read()).replace(',', ' ').replace('[', ' ').replace(']', ' ').split()]
        print(mergesort(nums))
        print(quicksort(nums))


if __name__ == "__main__":
    main(sys.argv[1:])
