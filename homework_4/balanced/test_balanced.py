import random
import unittest

from balanced import Node, draw, from_level_order, is_balanced, parse, solve


def height(node: Node | None) -> int:
    return (
        0 if node is None else 1 + max(height(node.left), height(node.right))
    )


def brute(node: Node | None) -> bool:
    if node is None:
        return True
    if abs(height(node.left) - height(node.right)) > 1:
        return False
    return brute(node.left) and brute(node.right)


def random_tree(n: int) -> Node | None:
    if n == 0:
        return None
    left = random.randint(0, n - 1)
    return Node(n, random_tree(left), random_tree(n - 1 - left))


def complete(n: int) -> Node | None:
    return from_level_order(list(range(1, n + 1)))


def fibonacci_tree(h: int) -> Node | None:
    if h <= 0:
        return None
    return Node(h, fibonacci_tree(h - 1), fibonacci_tree(h - 2))


def chain(n: int) -> Node | None:
    root = None
    for value in range(n):
        root = Node(value, None, root)
    return root


class TestBalanced(unittest.TestCase):
    def test_leetcode_examples(self):
        self.assertTrue(is_balanced(parse("[3,9,20,null,null,15,7]")))
        self.assertFalse(is_balanced(parse("[1,2,2,3,3,null,null,4,4]")))
        self.assertTrue(is_balanced(parse("[]")))

    def test_empty_and_single(self):
        self.assertTrue(is_balanced(None))
        self.assertTrue(is_balanced(Node(1)))

    def test_small_chains(self):
        self.assertTrue(is_balanced(chain(2)))
        self.assertTrue(is_balanced(parse("1 2")))
        self.assertFalse(is_balanced(chain(3)))
        self.assertFalse(is_balanced(parse("1 2 null 3")))

    def test_root_ok_but_inner_node_not(self):
        self.assertFalse(
            is_balanced(parse("1 2 3 4 5 null 6 7 null null null null 8"))
        )
        self.assertFalse(
            is_balanced(parse("1 2 3 4 null null 5 6 null null 7"))
        )

    def test_difference_exactly_one(self):
        self.assertTrue(is_balanced(parse("1 2 3 4")))
        self.assertTrue(is_balanced(parse("1 2 3 4 5 6 null 7")))
        self.assertFalse(is_balanced(parse("1 2 3 4 null null null 5")))

    def test_values_do_not_matter(self):
        self.assertTrue(is_balanced(parse("0 0 0 0 0 0 0")))
        self.assertTrue(is_balanced(Node("a", Node("b"), Node("c"))))

    def test_complete_trees(self):
        for n in range(200):
            self.assertTrue(is_balanced(complete(n)), n)

    def test_fibonacci_trees(self):
        for h in range(1, 20):
            root = fibonacci_tree(h)
            self.assertTrue(is_balanced(root), h)
            self.assertEqual(height(root), h)
            if h >= 3:
                broken = Node(0, fibonacci_tree(h - 1), fibonacci_tree(h - 3))
                self.assertFalse(is_balanced(broken), h)

    def test_against_brute(self):
        random.seed(0)
        for _ in range(3000):
            root = random_tree(random.randint(0, 12))
            self.assertEqual(is_balanced(root), brute(root), draw(root))

    def test_deep_chain(self):
        self.assertFalse(is_balanced(chain(100_000)))

    def test_deep_two_chains(self):
        n = 50_000
        self.assertFalse(is_balanced(Node(0, chain(n), chain(n))))

    def test_big_complete(self):
        self.assertTrue(is_balanced(complete(2**17 + 12345)))

    def test_big_fibonacci(self):
        self.assertTrue(is_balanced(fibonacci_tree(25)))

    def test_parse_formats(self):
        for text in (
            "3 9 20 null null 15 7",
            "[3,9,20,null,null,15,7]",
            "3,9,20,None,None,15,7",
        ):
            root = parse(text)
            self.assertEqual(root.value, 3)
            self.assertEqual((root.left.value, root.right.value), (9, 20))
            self.assertIsNone(root.left.left)
            self.assertEqual(
                (root.right.left.value, root.right.right.value), (15, 7)
            )

    def test_parse_empty(self):
        self.assertIsNone(parse(""))
        self.assertIsNone(parse("null"))

    def test_solve(self):
        self.assertTrue(solve("[3,9,20,null,null,15,7]"))
        self.assertFalse(solve("1 2 2 3 3 null null 4 4"))
        self.assertTrue(solve(""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
