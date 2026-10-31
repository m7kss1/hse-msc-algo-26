import random
import unittest

from avl import AVL


def check(node, low=None, high=None):
    if node is None:
        return 0, []
    if low is not None:
        assert low < node.value
    if high is not None:
        assert node.value < high
    lh, left = check(node.left, low, node.value)
    rh, right = check(node.right, node.value, high)
    assert abs(lh - rh) <= 1
    assert node.height == 1 + max(lh, rh)
    return node.height, left + [node.value] + right


class TestAVL(unittest.TestCase):
    def test_rotations(self):
        for values in ([3, 2, 1], [1, 2, 3], [3, 1, 2], [1, 3, 2]):
            tree = AVL()
            for value in values:
                tree.insert(value)
            self.assertEqual(tree.root.value, 2)
            self.assertEqual(check(tree.root)[1], [1, 2, 3])

    def test_delete_and_duplicates(self):
        tree = AVL()
        tree.delete(99)
        self.assertIsNone(tree.search(1))
        for value in (4, 2, 6, 1, 3, 5, 7, 4):
            tree.insert(value)
        for value in (4, 1, 6, 99, 2, 3, 5, 7):
            tree.delete(value)
            check(tree.root)
            self.assertIsNone(tree.search(value))
        self.assertIsNone(tree.root)

    def test_random_operations(self):
        rng = random.Random(0)
        tree, expected = AVL(), set()
        for _ in range(5000):
            value = rng.randrange(200)
            if rng.randrange(2):
                tree.insert(value)
                expected.add(value)
            else:
                tree.delete(value)
                expected.discard(value)
            self.assertEqual(check(tree.root)[1], sorted(expected))
            self.assertEqual(tree.search(value) is not None, value in expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
