import random
import unittest

from iterative import mergesort, quicksort


class TestSorts(unittest.TestCase):
    def test_examples_and_boundaries(self):
        cases = ([], [1], [2, 1], [4, 1, 3, 2, 3], [1] * 1000,
                 list(range(1000)), list(range(1000, 0, -1)))
        for nums in cases:
            for sort in (mergesort, quicksort):
                original = nums.copy()
                self.assertEqual(sort(nums), sorted(nums))
                self.assertEqual(nums, original)

    def test_random(self):
        rng = random.Random(42)
        for _ in range(300):
            nums = [rng.randrange(-20, 21) for _ in range(rng.randrange(100))]
            for sort in (mergesort, quicksort):
                self.assertEqual(sort(nums), sorted(nums))

    def test_large_array(self):
        rng = random.Random(123)
        nums = [rng.randrange(1000) for _ in range(10_000)]
        for sort in (mergesort, quicksort):
            self.assertEqual(sort(nums), sorted(nums))


if __name__ == "__main__":
    unittest.main(verbosity=2)
