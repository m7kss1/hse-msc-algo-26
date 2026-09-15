import itertools
import random
import unittest

from sum import max_even_sum, solve


def brute_force(nums: list[int]) -> int:
    best = 0
    for k in range(len(nums) + 1):
        for combo in itertools.combinations(nums, k):
            if sum(combo) % 2 == 0:
                best = max(best, sum(combo))
    return best


class TestMaxEvenSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solve("5 7 13 2 14"), 36)
        self.assertEqual(solve("3"), 0)

    def test_positive_only(self):
        self.assertEqual(max_even_sum([2, 4, 6]), 12)
        self.assertEqual(max_even_sum([1, 3, 5]), 8)
        self.assertEqual(max_even_sum([9, 4, 1, 3]), 16)

    def test_negatives_ignored(self):
        self.assertEqual(max_even_sum([-10, 12]), 12)
        self.assertEqual(max_even_sum([-7, -2, 4, 8]), 12)

    def test_negative_fixes_parity(self):
        self.assertEqual(max_even_sum([-1, 5]), 4)
        self.assertEqual(max_even_sum([5, 7, 13, 2, 14, -1, -8]), 40)

    def test_drop_is_cheaper(self):
        self.assertEqual(max_even_sum([1, 4, -5]), 4)

    def test_no_positive_answer(self):
        self.assertEqual(max_even_sum([-3, -5]), 0)
        self.assertEqual(max_even_sum([-4]), 0)
        self.assertEqual(max_even_sum([]), 0)

    def test_zeros(self):
        self.assertEqual(max_even_sum([0, 0]), 0)
        self.assertEqual(max_even_sum([0, 3]), 0)
        self.assertEqual(max_even_sum([0, 3, 5]), 8)

    def test_against_brute_force(self):
        random.seed(0)
        for _ in range(200):
            nums = [random.randint(-15, 15) for _ in range(random.randint(0, 9))]
            self.assertEqual(max_even_sum(nums), brute_force(nums), nums)


if __name__ == "__main__":
    unittest.main(verbosity=2)
