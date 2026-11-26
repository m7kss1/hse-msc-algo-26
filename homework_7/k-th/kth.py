"""Задача 2. K-й по величине элемент через minheap"""

import heapq
import sys


def sift_down(heap: list, i: int) -> None:
    """Опускать heap[i], пока он больше меньшего из детей"""
    n = len(heap)
    while True:
        smallest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest == i:
            return
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest


def heapify(heap: list) -> None:
    """Построить minheap на месте снизу вверх за O(len)"""
    for i in range(len(heap) // 2 - 1, -1, -1):
        sift_down(heap, i)


def heapreplace(heap: list, value) -> None:
    """Заменить минимум на value и восстановить кучу за O(log len)"""
    heap[0] = value
    sift_down(heap, 0)


def check_k(nums: list, k: int) -> None:
    if not 1 <= k <= len(nums):
        raise ValueError("k должно быть от 1 до длины массива")


def kth_largest(nums: list, k: int):
    """Своя куча: держим k наибольших элементов, минимум из них это ответ"""
    check_k(nums, k)
    heap = nums[:k]
    heapify(heap)
    for i in range(k, len(nums)):  # без среза nums[k:], чтобы не копировать хвост
        if nums[i] > heap[0]:
            heapreplace(heap, nums[i])
    return heap[0]


def kth_largest_heapq(nums: list, k: int):
    """То же самое на heapq"""
    check_k(nums, k)
    heap = nums[:k]
    heapq.heapify(heap)
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heapreplace(heap, nums[i])
    return heap[0]


def trace(nums: list, k: int) -> None:
    check_k(nums, k)
    heap = nums[:k]
    heapify(heap)
    print(f"nums = {nums}, k = {k}")
    print(f"куча из первых {k}: {nums[:k]} -> {heap}, вершина {heap[0]}")
    width = max(len(str(sorted(heap))), len("куча"))
    print(f"\n{'i':>3} | элемент | {'действие':<24} | {'куча':<{width}} | вершина")
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            action = f"{nums[i]} > {heap[0]}, меняем вершину"
            heapreplace(heap, nums[i])
        else:
            action = f"{nums[i]} <= {heap[0]}, пропускаем"
        print(f"{i:>3} | {nums[i]:>7} | {action:<24} | {str(heap):<{width}} | {heap[0]}")
    print(f"\nответ: {heap[0]}")


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
        trace(*parse(" ".join(argv[1:]) or "3 2 3 1 2 4 5 5 6 / 4"))
        return
    nums, k = parse(" ".join(argv) if argv else sys.stdin.read())
    print(kth_largest(nums, k))
    print(kth_largest_heapq(nums, k))


if __name__ == "__main__":
    main(sys.argv[1:])
