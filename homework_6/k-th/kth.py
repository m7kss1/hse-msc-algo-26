"""Задача 3. K-й по величине элемент"""

import sys


def partition(arr: list, left: int, right: int) -> tuple[int, int]:
    pivot = arr[(left + right) // 2]
    low, i, high = left, left, right
    while i <= high:
        if arr[i] < pivot:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1  # элемент на i после обмена еще не проверен
        else:
            i += 1
    return low, high


def kth_largest(nums: list, k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError("k должно быть от 1 до длины массива")
    arr = nums.copy()  # переставляем элементы только в копии
    target = len(arr) - k
    left, right = 0, len(arr) - 1
    while left <= right:
        low, high = partition(arr, left, right)
        if target < low:
            right = low - 1
        elif target > high:
            left = high + 1
        else:
            return arr[target]  # искомый индекс попал в блок равных


def trace(nums: list, k: int) -> None:
    if not 1 <= k <= len(nums):
        raise ValueError("k должно быть от 1 до длины массива")
    arr = nums.copy()
    target = len(arr) - k
    left, right = 0, len(arr) - 1
    print(f"nums = {nums}, k = {k}, индекс по возрастанию = {target}")
    step = 0
    while left <= right:
        step += 1
        pivot = arr[(left + right) // 2]
        low, high = partition(arr, left, right)
        print(f"{step}: [{left}, {right}], опорный {pivot}, {arr}, равные [{low}, {high}]")
        if target < low:
            print("   ищем слева")
            right = low - 1
        elif target > high:
            print("   ищем справа")
            left = high + 1
        else:
            print(f"ответ: {arr[target]}")
            return


def parse(text: str) -> tuple[list[int], int]:
    """Массив и k, разделенные / или переводом строки"""
    parts = [part.strip() for part in text.replace("\n", "/").split("/") if part.strip()]
    if len(parts) != 2:
        raise ValueError("нужны массив и k, разделенные '/'")
    for ch in "[],":
        parts[0] = parts[0].replace(ch, " ")
    return [int(x) for x in parts[0].split()], int(parts[1])


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        text = " ".join(argv[1:]) or "3 2 3 1 2 4 5 5 6 / 4"
        trace(*parse(text))
        return
    print(kth_largest(*parse(" ".join(argv) if argv else sys.stdin.read())))


if __name__ == "__main__":
    main(sys.argv[1:])
