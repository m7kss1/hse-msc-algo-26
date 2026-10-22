import random
import unittest

from validate_bst import (
    Node,
    draw,
    from_level_order,
    is_valid_bst,
    parse,
    solve,
)


def brute(root: Node | None) -> bool:

    def values(node: Node | None) -> list:
        return (
            []
            if node is None
            else values(node.left) + [node.value] + values(node.right)
        )

    def check(node: Node | None) -> bool:
        if node is None:
            return True
        if any(v >= node.value for v in values(node.left)):
            return False
        if any(v <= node.value for v in values(node.right)):
            return False
        return check(node.left) and check(node.right)

    return check(root)


def random_tree(n: int, low: int, high: int) -> Node | None:
    if n == 0:
        return None
    left = random.randint(0, n - 1)
    return Node(
        random.randint(low, high),
        random_tree(left, low, high),
        random_tree(n - 1 - left, low, high),
    )


def random_bst(lo: int, hi: int) -> Node | None:
    if lo >= hi or random.random() < 0.2:
        return None
    mid = random.randint(lo, hi - 1)
    return Node(mid, random_bst(lo, mid), random_bst(mid + 1, hi))


class TestValidateBST(unittest.TestCase):
    def test_leetcode_examples(self):
        self.assertTrue(is_valid_bst(parse("[2,1,3]")))
        self.assertFalse(is_valid_bst(parse("[5,1,4,null,null,3,6]")))

    def test_empty_and_single(self):
        self.assertTrue(is_valid_bst(None))
        self.assertTrue(is_valid_bst(Node(0)))
        self.assertTrue(is_valid_bst(Node(-(10**18))))

    def test_two_nodes(self):
        self.assertTrue(is_valid_bst(Node(2, Node(1))))
        self.assertTrue(is_valid_bst(Node(2, None, Node(3))))
        self.assertFalse(is_valid_bst(Node(2, Node(3))))
        self.assertFalse(is_valid_bst(Node(2, None, Node(1))))

    def test_duplicates_are_invalid(self):
        self.assertFalse(is_valid_bst(parse("2 2 2")))
        self.assertFalse(is_valid_bst(parse("2 2")))
        self.assertFalse(is_valid_bst(parse("2 null 2")))
        self.assertFalse(is_valid_bst(parse("5 3 8 1 5")))

    def test_violation_deep_in_subtree(self):
        self.assertFalse(
            is_valid_bst(parse("8 3 10 1 6 null 14 null null 4 9"))
        )
        self.assertFalse(is_valid_bst(parse("5 4 6 null null 3 7")))
        self.assertFalse(
            is_valid_bst(parse("10 5 15 null null 12 20 null null 17 null 14"))
        )

    def test_valid_trees(self):
        self.assertTrue(
            is_valid_bst(parse("8 3 10 1 6 null 14 null null 4 7 13"))
        )
        self.assertTrue(
            is_valid_bst(parse("10 5 15 null null 12 20 null null 17 null 16"))
        )
        self.assertTrue(is_valid_bst(parse("0 -10 10 -20 -5 5 20")))

    def test_chains(self):
        self.assertTrue(is_valid_bst(parse("1 null 2 null 3 null 4")))
        self.assertTrue(is_valid_bst(parse("4 3 null 2 null 1")))
        self.assertTrue(is_valid_bst(parse("1 null 5 4 null 2 null null 3")))
        self.assertFalse(is_valid_bst(parse("1 null 5 4 null 6")))

    def test_extreme_values(self):
        lo, hi = -(2**63), 2**63 - 1
        self.assertTrue(is_valid_bst(Node(lo, None, Node(hi))))
        self.assertTrue(is_valid_bst(Node(hi, Node(lo))))
        self.assertFalse(is_valid_bst(Node(lo, Node(lo))))
        self.assertFalse(is_valid_bst(Node(hi, None, Node(hi))))

    def test_strings(self):
        self.assertTrue(
            is_valid_bst(Node("m", Node("c", Node("a"), Node("f")), Node("x")))
        )
        self.assertFalse(
            is_valid_bst(Node("m", Node("c", Node("a"), Node("z")), Node("x")))
        )

    def test_deep_chain(self):
        n = 100_000
        root = None
        for value in range(n):
            root = Node(value, root)
        self.assertTrue(is_valid_bst(root))
        root.left.left.value = n
        self.assertFalse(is_valid_bst(root))

    def test_big_balanced(self):
        n = 2**17 - 1
        values = list(range(n))

        def build(lo: int, hi: int) -> Node | None:
            if lo >= hi:
                return None
            mid = (lo + hi) // 2
            return Node(values[mid], build(lo, mid), build(mid + 1, hi))

        root = build(0, n)
        self.assertTrue(is_valid_bst(root))
        values[n // 2 + 1] = -1
        self.assertFalse(is_valid_bst(build(0, n)))

    def test_random_bst_valid(self):
        random.seed(0)
        for _ in range(300):
            self.assertTrue(is_valid_bst(random_bst(-30, 30)))

    def test_against_brute(self):
        random.seed(1)
        for _ in range(3000):
            root = random_tree(random.randint(0, 8), -5, 5)
            self.assertEqual(is_valid_bst(root), brute(root), draw(root))

    def test_parse_formats(self):
        for text in (
            "5 1 4 null null 3 6",
            "[5,1,4,null,null,3,6]",
            "5,1,4,None,None,3,6",
        ):
            root = parse(text)
            self.assertEqual(root.value, 5)
            self.assertEqual((root.left.value, root.right.value), (1, 4))
            self.assertIsNone(root.left.left)
            self.assertEqual(
                (root.right.left.value, root.right.right.value), (3, 6)
            )

    def test_parse_empty(self):
        self.assertIsNone(parse(""))
        self.assertIsNone(parse("[]"))
        self.assertIsNone(parse("null"))

    def test_parse_trailing_nulls(self):
        root = from_level_order([1, None, 2, None, None])
        self.assertIsNone(root.left)
        self.assertEqual(root.right.value, 2)

    def test_parse_numbers_not_strings(self):
        self.assertTrue(solve("9 null 10"))

    def test_solve(self):
        self.assertTrue(solve("[2,1,3]"))
        self.assertFalse(solve("[5,1,4,null,null,3,6]"))
        self.assertTrue(solve(""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
