import io
import random
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from compare import mergesort, quicksort, timer


class TestSorts(unittest.TestCase):
    def test_examples_and_boundaries(self):
        for nums in ([], [1], [3, 2, 1], [1, 1, 1], [0, -3, 4, -3, 0], list(range(300)), list(range(300, 0, -1))):
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

    def test_timer(self):
        @timer
        def add(a, b=0):
            return a + b
        out = io.StringIO()
        with patch("compare.perf_counter", side_effect=[10.0, 10.25]), redirect_stdout(out):
            self.assertEqual(add(2, b=3), 5)
        self.assertEqual(add.__name__, "add")
        self.assertEqual(out.getvalue(), "add: 0.250000 с\n")

    def test_timer_exception(self):
        @timer
        def fail():
            raise ValueError("ошибка")
        with redirect_stdout(io.StringIO()) as out:
            with self.assertRaises(ValueError):
                fail()
        self.assertIn("fail:", out.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
