import random
import unittest

from makeheap import count_swaps, is_min_heap, makeheap, makeheap_n_log_n, parse

BUILDS = (makeheap_n_log_n, makeheap)


class TestMakeheap(unittest.TestCase):
    def check(self, nums: list) -> None:
        for build in BUILDS:
            arr = nums.copy()
            self.assertIsNone(build(arr))  # куча строится на месте
            self.assertTrue(is_min_heap(arr), (build.__name__, nums, arr))
            self.assertEqual(sorted(arr), sorted(nums))  # те же элементы
            if arr:
                self.assertEqual(arr[0], min(nums))

    def test_boundaries(self):
        for nums in ([], [1], [2, 1], [1, 2], [3, 3, 3], [0, -5, 5, -5, 0],
                     [7, 6, 5, 4, 3, 2, 1], [1.5, -2.0, 0.0], list(range(1000)),
                     list(range(1000, 0, -1)), [1] * 1000):
            self.check(nums)

    def test_random(self):
        rng = random.Random(42)
        for _ in range(500):
            self.check([rng.randrange(-20, 21) for _ in range(rng.randrange(200))])

    def test_is_min_heap(self):
        self.assertTrue(is_min_heap([]))
        self.assertTrue(is_min_heap([1, 3, 2, 5, 9, 8, 7]))
        self.assertFalse(is_min_heap([2, 1]))
        self.assertFalse(is_min_heap([1, 3, 2, 0]))

    def test_trace_example(self):
        nums = [7, 6, 5, 4, 3, 2, 1]
        arr = nums.copy()
        makeheap_n_log_n(arr)
        self.assertEqual(arr, [1, 4, 2, 7, 5, 6, 3])
        arr = nums.copy()
        makeheap(arr)
        self.assertEqual(arr, [1, 3, 2, 4, 6, 7, 5])

    def test_swaps_linear(self):
        """Обменов не больше суммы высот узлов, а она меньше n"""
        rng = random.Random(7)
        for n in (1, 2, 3, 10, 100, 1000, 5000):
            cases = (list(range(n, 0, -1)), [rng.randrange(n) for _ in range(n)])
            for nums in cases:
                self.assertLess(count_swaps(makeheap, nums), n)

    def test_swaps_worst_n_log_n(self):
        """На убывающем массиве каждый элемент поднимается до корня"""
        for n in (1, 2, 7, 100, 5000):
            nums = list(range(n, 0, -1))
            depths = sum((i + 1).bit_length() - 1 for i in range(n))
            self.assertEqual(count_swaps(makeheap_n_log_n, nums), depths)
        self.assertGreater(count_swaps(makeheap_n_log_n, list(range(5000, 0, -1))), 10 * 5000)

    def test_parse(self):
        self.assertEqual(parse("[5, 3, 8]"), [5, 3, 8])
        self.assertEqual(parse("5 3\n8"), [5, 3, 8])
        self.assertEqual(parse(""), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
