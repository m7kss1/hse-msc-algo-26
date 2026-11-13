import random
import unittest

from kth import kth_largest, parse


class TestKth(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_boundaries_and_duplicates(self):
        for nums in ([1], [2, 2, 2], [-4, -1, 0, -1], list(range(100)), list(range(100, 0, -1))):
            original = nums.copy()
            for k in range(1, len(nums) + 1):
                self.assertEqual(kth_largest(nums, k), sorted(nums, reverse=True)[k - 1])
            self.assertEqual(nums, original)
        for nums, k in (([], 1), ([1], 0), ([1], 2), ([1], -1)):
            with self.assertRaises(ValueError):
                kth_largest(nums, k)

    def test_random(self):
        rng = random.Random(42)
        for _ in range(500):
            nums = [rng.randrange(-10, 11) for _ in range(rng.randrange(1, 100))]
            k = rng.randint(1, len(nums))
            self.assertEqual(kth_largest(nums, k), sorted(nums, reverse=True)[k - 1])

    def test_parse(self):
        self.assertEqual(parse('[3,2,1,5,6,4] / 2'), ([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(parse('3 2 1\n2'), ([3, 2, 1], 2))
        with self.assertRaises(ValueError):
            parse('1 2 3')


if __name__ == "__main__":
    unittest.main(verbosity=2)
