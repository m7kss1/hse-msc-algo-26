import builtins
import random
import tracemalloc
import unittest
from unittest.mock import patch

from heapsort import build_max_heap, heapsort, mergesort, parse


class TestHeapsort(unittest.TestCase):
    def check(self, nums: list) -> None:
        arr = nums.copy()
        self.assertIsNone(heapsort(arr))  # сортировка на месте, как list.sort
        self.assertEqual(arr, sorted(nums))

    def test_examples_and_boundaries(self):
        for nums in ([], [1], [2, 1], [1, 2], [3, 3, 3], [4, 1, 3, 2, 3], [5, 2, 9, 1, 7, 3, 8],
                     [0, -3, 4, -3, 0], [2.5, -1.0, 0.0, 2.5], [10**18, -10**18, 0],
                     list(range(1000)), list(range(1000, 0, -1)), [7] * 1000):
            self.check(nums)

    def test_strings(self):
        self.check(["pear", "apple", "fig", "banana", "apple"])

    def test_random(self):
        rng = random.Random(42)
        for _ in range(500):
            self.check([rng.randrange(-20, 21) for _ in range(rng.randrange(200))])

    def test_large(self):
        rng = random.Random(123)
        self.check([rng.randrange(10**9) for _ in range(50_000)])

    def test_in_place(self):
        """Сортируется переданный список, дополнительный массив не создается"""
        rng = random.Random(3)
        arr = [rng.randrange(10**9) for _ in range(20_000)]
        expected = sorted(arr)
        tracemalloc.start()
        heapsort(arr)
        peak = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        self.assertEqual(arr, expected)
        self.assertLess(peak, 4096)  # копия списка заняла бы ~160 КБ

    def test_does_not_use_sorted(self):
        rng = random.Random(5)
        nums = [rng.randrange(100) for _ in range(300)]
        arr = nums.copy()
        with patch.object(builtins, "sorted", side_effect=AssertionError("sorted вызван")):
            heapsort(arr)
        self.assertEqual(arr, sorted(nums))

    def test_build_max_heap(self):
        rng = random.Random(9)
        for _ in range(200):
            arr = [rng.randrange(50) for _ in range(rng.randrange(1, 100))]
            build_max_heap(arr)
            self.assertTrue(all(arr[(i - 1) // 2] >= arr[i] for i in range(1, len(arr))))

    def test_mergesort(self):
        rng = random.Random(1)
        for _ in range(200):
            nums = [rng.randrange(-20, 21) for _ in range(rng.randrange(100))]
            original = nums.copy()
            self.assertEqual(mergesort(nums), sorted(nums))
            self.assertEqual(nums, original)

    def test_parse(self):
        self.assertEqual(parse("[5, 2, 9]"), [5, 2, 9])
        self.assertEqual(parse("5 2\n9"), [5, 2, 9])
        self.assertEqual(parse(""), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
