import heapq
import random
import unittest
from unittest.mock import patch

from kth import heapify, heapreplace, kth_largest, kth_largest_heapq, parse

SOLUTIONS = (kth_largest, kth_largest_heapq)


def expected(nums: list, k: int):
    return sorted(nums, reverse=True)[k - 1]


def is_min_heap(arr: list) -> bool:
    return all(arr[(i - 1) // 2] <= arr[i] for i in range(1, len(arr)))


class TestKth(unittest.TestCase):
    def test_examples(self):
        for solve in SOLUTIONS:
            self.assertEqual(solve([3, 2, 1, 5, 6, 4], 2), 5)
            self.assertEqual(solve([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_boundaries_and_duplicates(self):
        for nums in ([1], [2, 2, 2], [-4, -1, 0, -1], [5, 1, 9, 3, 7, 2, 8, 6, 4],
                     [1.5, -0.5, 2.5], list(range(100)), list(range(100, 0, -1))):
            original = nums.copy()
            for k in range(1, len(nums) + 1):  # k = 1 это максимум, k = n это минимум
                for solve in SOLUTIONS:
                    self.assertEqual(solve(nums, k), expected(nums, k))
            self.assertEqual(nums, original)  # входной массив не меняется

    def test_invalid_k(self):
        for nums, k in (([], 1), ([1], 0), ([1], 2), ([1], -1)):
            for solve in SOLUTIONS:
                with self.assertRaises(ValueError):
                    solve(nums, k)

    def test_random(self):
        rng = random.Random(42)
        for _ in range(500):
            nums = [rng.randrange(-10, 11) for _ in range(rng.randrange(1, 100))]
            k = rng.randint(1, len(nums))
            for solve in SOLUTIONS:
                self.assertEqual(solve(nums, k), expected(nums, k))

    def test_large(self):
        rng = random.Random(7)
        nums = [rng.randrange(10**9) for _ in range(50_000)]
        for k in (1, 10, 1000, 50_000):
            for solve in SOLUTIONS:
                self.assertEqual(solve(nums, k), expected(nums, k))

    def test_own_heap_does_not_use_heapq(self):
        with patch("kth.heapq.heapify", side_effect=AssertionError), \
                patch("kth.heapq.heapreplace", side_effect=AssertionError):
            self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_own_heap_matches_heapq(self):
        rng = random.Random(1)
        for _ in range(300):
            nums = [rng.randrange(-50, 51) for _ in range(rng.randrange(1, 60))]
            own, ref = nums.copy(), nums.copy()
            heapify(own)
            heapq.heapify(ref)
            self.assertTrue(is_min_heap(own))
            self.assertEqual(sorted(own), sorted(ref))  # раскладка у heapq может отличаться
            for _ in range(20):
                value = rng.randrange(-50, 51)
                heapreplace(own, value)
                heapq.heapreplace(ref, value)
                self.assertTrue(is_min_heap(own))
                self.assertEqual(own[0], ref[0])
                self.assertEqual(sorted(own), sorted(ref))

    def test_parse(self):
        self.assertEqual(parse("[3,2,1,5,6,4] / 2"), ([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(parse("3 2 1\n2"), ([3, 2, 1], 2))
        with self.assertRaises(ValueError):
            parse("1 2 3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
