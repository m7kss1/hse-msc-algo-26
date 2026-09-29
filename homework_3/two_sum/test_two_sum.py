import random
import unittest

from two_sum import solve, two_sum


def brute(arr: list[int], k: int) -> tuple[int, int] | None:
    for j in range(len(arr)):
        for i in range(j):
            if arr[i] + arr[j] == k:
                return i, j
    return None


class TestTwoSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(two_sum([1, 3, 4, 10], 7), (1, 2))
        self.assertEqual(two_sum([5, 5, 1, 4], 10), (0, 1))

    def test_no_pair(self):
        self.assertIsNone(two_sum([], 0))
        self.assertIsNone(two_sum([1, 2, 3], 100))

    def test_element_not_used_twice(self):
        self.assertIsNone(two_sum([5], 10))
        self.assertIsNone(two_sum([5, 1], 10))
        self.assertEqual(two_sum([3, 1, 3], 6), (0, 2))

    def test_pair_at_ends(self):
        self.assertEqual(two_sum([1, 8, 9, 2], 3), (0, 3))

    def test_indices_ascending(self):
        i, j = two_sum([10, 20, 30, 1], 11)
        self.assertLess(i, j)
        self.assertEqual((i, j), (0, 3))

    def test_negatives_and_zeros(self):
        self.assertEqual(two_sum([-3, 4, 3, 90], 0), (0, 2))
        self.assertEqual(two_sum([0, 4, 3, 0], 0), (0, 3))
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), (2, 4))

    def test_big_numbers(self):
        big = 10**18
        self.assertEqual(two_sum([big, 1, -big + 5], 5), (0, 2))

    def test_several_pairs(self):
        self.assertEqual(two_sum([1, 2, 3, 4], 5), (1, 2))
        self.assertEqual(two_sum([2, 2, 2], 4), (0, 1))

    def test_solve_text(self):
        self.assertEqual(solve("1 3 4 10 / 7"), "1 2")
        self.assertEqual(solve("5 5 1 4\n10\n"), "0 1")
        self.assertEqual(solve("1 2 / 10"), "пары нет")

    def test_big(self):
        n = 200_000
        arr = list(range(0, 2 * n, 2))
        self.assertEqual(two_sum(arr, arr[-1] + arr[-2]), (n - 2, n - 1))

    def test_against_brute(self):
        random.seed(0)
        for _ in range(2000):
            arr = [random.randint(-10, 10) for _ in range(random.randint(0, 10))]
            k = random.randint(-20, 20)
            self.assertEqual(two_sum(arr, k), brute(arr, k), (arr, k))


if __name__ == "__main__":
    unittest.main(verbosity=2)
