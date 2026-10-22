import random
import unittest

from traversal import (
    BST,
    Node,
    TRAVERSALS,
    draw,
    inorder,
    postorder,
    preorder,
    reverse_inorder,
    reverse_postorder,
    reverse_preorder,
    solve,
)


def recursive(node: Node | None, order: str) -> list:
    if node is None:
        return []
    parts = {
        "N": lambda: [node.value],
        "L": lambda: recursive(node.left, order),
        "R": lambda: recursive(node.right, order),
    }
    return [value for part in order for value in parts[part]()]


def is_bst(node: Node | None, low=None, high=None) -> bool:
    if node is None:
        return True
    if low is not None and node.value < low:
        return False
    if high is not None and node.value >= high:
        return False
    return is_bst(node.left, low, node.value) and is_bst(
        node.right, node.value, high
    )


def height(node: Node | None) -> int:
    return (
        0 if node is None else 1 + max(height(node.left), height(node.right))
    )


ORDERS = {
    preorder: "NLR",
    inorder: "LNR",
    postorder: "LRN",
    reverse_preorder: "NRL",
    reverse_inorder: "RNL",
    reverse_postorder: "RLN",
}

WIKI = "F B G A D I C E H".split()


class TestTraversal(unittest.TestCase):
    def test_insert_empty(self):
        tree = BST()
        self.assertIsNone(tree.root)
        self.assertEqual(len(tree), 0)

    def test_insert_single(self):
        tree = BST([5])
        self.assertEqual(tree.root.value, 5)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)

    def test_shape(self):
        root = BST(WIKI).root
        self.assertEqual(root.value, "F")
        self.assertEqual((root.left.value, root.right.value), ("B", "G"))
        self.assertEqual(
            (root.left.left.value, root.left.right.value), ("A", "D")
        )
        d = root.left.right
        self.assertEqual((d.left.value, d.right.value), ("C", "E"))
        self.assertIsNone(root.right.left)
        self.assertEqual(root.right.right.value, "I")
        self.assertEqual(root.right.right.left.value, "H")

    def test_returns_new_node(self):
        tree = BST([5, 3])
        node = tree.insert(4)
        self.assertIs(tree.root.left.right, node)
        self.assertEqual(len(tree), 3)

    def test_duplicates_go_right(self):
        tree = BST([5, 5, 5])
        self.assertIsNone(tree.root.left)
        self.assertEqual(tree.root.right.value, 5)
        self.assertEqual(tree.root.right.right.value, 5)
        self.assertEqual(len(tree), 3)
        self.assertEqual(inorder(BST([3, 1, 3, 2, 1]).root), [1, 1, 2, 3, 3])

    def test_sorted_input_is_a_chain(self):
        root = BST(range(10)).root
        self.assertEqual(height(root), 10)
        self.assertIsNone(root.left)

    def test_random_keeps_invariant(self):
        random.seed(1)
        for _ in range(300):
            values = [
                random.randint(-10, 10) for _ in range(random.randint(0, 30))
            ]
            tree = BST(values)
            self.assertTrue(is_bst(tree.root), values)
            self.assertEqual(len(tree), len(values))

    def test_wikipedia(self):
        root = BST(WIKI).root
        expected = {
            preorder: "F B A D C E G I H",
            inorder: "A B C D E F G H I",
            postorder: "A C E D B H I G F",
            reverse_preorder: "F G I H B D E C A",
            reverse_inorder: "I H G F E D C B A",
            reverse_postorder: "H I G E C D A B F",
        }
        for walk, line in expected.items():
            self.assertEqual(walk(root), line.split(), walk.__name__)

    def test_numbers(self):
        root = BST([8, 3, 10, 1, 6, 14, 4, 7, 13]).root
        self.assertEqual(preorder(root), [8, 3, 1, 6, 4, 7, 10, 14, 13])
        self.assertEqual(inorder(root), [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(postorder(root), [1, 4, 7, 6, 3, 13, 14, 10, 8])

    def test_empty(self):
        for _, walk in TRAVERSALS:
            self.assertEqual(walk(None), [], walk.__name__)

    def test_single(self):
        for _, walk in TRAVERSALS:
            self.assertEqual(walk(Node(7)), [7], walk.__name__)

    def test_three_nodes(self):
        root = BST([2, 1, 3]).root
        self.assertEqual(preorder(root), [2, 1, 3])
        self.assertEqual(inorder(root), [1, 2, 3])
        self.assertEqual(postorder(root), [1, 3, 2])
        self.assertEqual(reverse_preorder(root), [2, 3, 1])
        self.assertEqual(reverse_inorder(root), [3, 2, 1])
        self.assertEqual(reverse_postorder(root), [3, 1, 2])

    def test_chains(self):
        right = BST([1, 2, 3]).root
        left = BST([3, 2, 1]).root
        self.assertEqual(preorder(right), [1, 2, 3])
        self.assertEqual(postorder(right), [3, 2, 1])
        self.assertEqual(preorder(left), [3, 2, 1])
        self.assertEqual(postorder(left), [1, 2, 3])
        self.assertEqual(inorder(left), inorder(right))

    def test_not_bst_tree(self):
        root = Node(1, Node(2, Node(4), Node(5)), Node(3))
        self.assertEqual(preorder(root), [1, 2, 4, 5, 3])
        self.assertEqual(inorder(root), [4, 2, 5, 1, 3])
        self.assertEqual(postorder(root), [4, 5, 2, 3, 1])

    def test_inorder_sorts(self):
        random.seed(2)
        for _ in range(300):
            values = [
                random.randint(-50, 50) for _ in range(random.randint(0, 40))
            ]
            root = BST(values).root
            self.assertEqual(inorder(root), sorted(values))
            self.assertEqual(
                reverse_inorder(root), sorted(values, reverse=True)
            )

    def test_reverse_relations(self):
        random.seed(3)
        for _ in range(300):
            root = BST(random.sample(range(100), random.randint(0, 30))).root
            self.assertEqual(reverse_preorder(root), postorder(root)[::-1])
            self.assertEqual(reverse_postorder(root), preorder(root)[::-1])
            self.assertEqual(reverse_inorder(root), inorder(root)[::-1])

    def test_against_recursive(self):
        random.seed(4)
        for _ in range(300):
            root = BST(
                [random.randint(0, 20) for _ in range(random.randint(0, 25))]
            ).root
            for walk, order in ORDERS.items():
                self.assertEqual(
                    walk(root), recursive(root, order), walk.__name__
                )

    def test_deep_chain(self):
        n = 100_000
        root = None
        for value in reversed(range(n)):
            root = Node(value, None, root)
        self.assertEqual(inorder(root), list(range(n)))
        self.assertEqual(postorder(root), list(range(n - 1, -1, -1)))
        self.assertEqual(reverse_inorder(root), list(range(n - 1, -1, -1)))

    def test_big_random(self):
        random.seed(5)
        values = random.sample(range(10**6), 100_000)
        root = BST(values).root
        self.assertEqual(inorder(root), sorted(values))
        self.assertEqual(preorder(root)[0], values[0])
        self.assertEqual(postorder(root)[-1], values[0])

    def test_solve(self):
        self.assertEqual(
            solve("2 1 3"),
            "preorder:          2 1 3\n"
            "inorder:           1 2 3\n"
            "postorder:         1 3 2\n"
            "reverse preorder:  2 3 1\n"
            "reverse inorder:   3 2 1\n"
            "reverse postorder: 3 1 2",
        )

    def test_solve_numbers(self):
        self.assertIn("inorder:           9 10", solve("10 9"))

    def test_solve_empty(self):
        self.assertTrue(
            all(line.endswith(":") for line in solve("").splitlines())
        )

    def test_draw(self):
        self.assertEqual(draw(None), ["(пустое дерево)"])
        self.assertEqual(draw(Node(1)), ["1"])
        self.assertEqual(draw(BST([2, 1, 3]).root), [" 2", "/ \\", "1 3"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
