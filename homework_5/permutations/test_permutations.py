import io
import itertools
import unittest
from contextlib import redirect_stdout

from permutations import permutations


class TestPermutations(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(permutations([1, 2, 3]), [
            [1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        self.assertEqual(permutations([0, 1]), [[0, 1], [1, 0]])
        self.assertEqual(permutations([1]), [[1]])
        self.assertEqual(permutations([]), [[]])

    def test_against_itertools(self):
        for nums in ([], [1, 1, 2], list(range(7))):
            original = nums.copy()
            self.assertEqual(permutations(nums), [list(p) for p in itertools.permutations(nums)])
            self.assertEqual(nums, original)

    def test_trace(self):
        out = io.StringIO()
        with redirect_stdout(out):
            result = permutations([1, 2], trace=True)
        self.assertEqual(result, [[1, 2], [2, 1]])
        self.assertIn('    -> step([1, 2])', out.getvalue())
        self.assertIn('    <- step = [1, 2]', out.getvalue())
        self.assertIn('<- step = []', out.getvalue())


if __name__ == '__main__':
    unittest.main(verbosity=2)
