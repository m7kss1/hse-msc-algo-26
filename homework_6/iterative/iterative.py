"""Задача 2. Итеративные сортировки"""

import sys


def mergesort(nums: list) -> list:
    result = nums.copy()
    n = len(result)
    buffer = [None] * n
    width = 1
    while width < n:
        for start in range(0, n, 2 * width):
            mid = min(start + width, n)
            end = min(start + 2 * width, n)
            i, j = start, mid
            for out in range(start, end):
                if i < mid and (j == end or result[i] <= result[j]):
                    buffer[out] = result[i]
                    i += 1
                else:
                    buffer[out] = result[j]
                    j += 1
        result, buffer = buffer, result
        width *= 2  # отсортированные отрезки стали вдвое длиннее
    return result


def partition(nums: list, left: int, right: int) -> tuple[int, int]:
    """Разбить включительный диапазон на меньше, равно и больше опорного"""
    pivot = nums[right]
    low, i, high = left, left, right
    while i <= high:
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1  # новый nums[i] еще не проверен
        else:
            i += 1
    return low, high


def quicksort(nums: list) -> list:
    result = nums.copy()
    stack = [(0, len(result) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        low, high = partition(result, left, right)
        # больший диапазон кладем первым, чтобы меньший обработался раньше
        parts = [(left, low - 1), (high + 1, right)]
        parts.sort(key=lambda part: part[1] - part[0], reverse=True)
        stack.extend(part for part in parts if part[0] < part[1])
    return result


def trace(nums: list) -> None:
    print(f"nums = {nums}")
    arr = nums.copy()
    width = 1
    print("\nmergesort: длина сливаемых отрезков")
    while width < len(arr):
        for start in range(0, len(arr), width * 2):
            mid = min(start + width, len(arr))
            end = min(start + width * 2, len(arr))
            # тот же проход слияния, что и в mergesort
            left, right = arr[start:mid], arr[mid:end]
            i = j = 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            arr[start:end] = merged + left[i:] + right[j:]
        print(f"  {width}: {arr}")
        width *= 2
    print("\nquicksort: диапазон, опорный, массив после разбиения")
    arr = nums.copy()
    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        pivot = arr[right]
        low, high = partition(arr, left, right)
        print(f"  [{left}, {right}], {pivot}: {arr}, равные [{low}, {high}]")
        parts = [(left, low - 1), (high + 1, right)]
        parts.sort(key=lambda part: part[1] - part[0], reverse=True)
        stack.extend(part for part in parts if part[0] < part[1])


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace([int(x) for x in argv[1:]] if len(argv) > 1 else [4, 1, 3, 2, 3])
        return
    text = " ".join(argv) if argv else sys.stdin.read()
    for ch in "[],":
        text = text.replace(ch, " ")
    nums = [int(x) for x in text.split()]
    print(mergesort(nums))
    print(quicksort(nums))


if __name__ == "__main__":
    main(sys.argv[1:])
