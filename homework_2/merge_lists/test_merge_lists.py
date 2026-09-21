import random
import unittest

from merge_lists import (
    Node,
    from_list,
    merge_with_dummy,
    merge_without_dummy,
    solve,
    to_list,
)

MERGES = (merge_with_dummy, merge_without_dummy)


def nodes_of(head: Node | None) -> list[Node]:
    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next
    return nodes


class TestMergeLists(unittest.TestCase):
    def check(self, values_a: list, values_b: list, expected: list) -> None:
        for merge in MERGES:
            merged = merge(from_list(values_a), from_list(values_b))
            self.assertEqual(to_list(merged), expected, merge.__name__)

    def test_example(self):
        self.check([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_empty(self):
        self.check([], [], [])
        self.check([], [1, 2], [1, 2])
        self.check([1, 2], [], [1, 2])

    def test_single(self):
        self.check([2], [1], [1, 2])
        self.check([1], [2], [1, 2])
        self.check([1], [1], [1, 1])

    def test_no_overlap(self):
        self.check([1, 2, 3], [7, 8, 9], [1, 2, 3, 7, 8, 9])
        self.check([7, 8, 9], [1, 2, 3], [1, 2, 3, 7, 8, 9])

    def test_different_lengths(self):
        self.check([1], [0, 2, 3, 4], [0, 1, 2, 3, 4])
        self.check([2, 5, 6, 9], [7], [2, 5, 6, 7, 9])

    def test_duplicates_and_negatives(self):
        self.check([1, 1, 1], [1, 1], [1, 1, 1, 1, 1])
        self.check([-5, -1, 0], [-3, 2], [-5, -3, -1, 0, 2])

    def test_reuses_nodes(self):
        for merge in MERGES:
            a, b = from_list([1, 3]), from_list([2, 4])
            original = nodes_of(a) + nodes_of(b)
            merged = nodes_of(merge(a, b))
            self.assertEqual(len(merged), 4)
            for node in merged:
                self.assertIn(node, original, merge.__name__)

    def test_input_heads_are_consumed(self):
        a = from_list([1, 5])
        b = from_list([2, 3])
        merged = merge_without_dummy(a, b)
        self.assertIs(merged, a)
        self.assertEqual(to_list(a), [1, 2, 3, 5])

    def test_strings(self):
        self.check(["a", "c"], ["b", "d"], ["a", "b", "c", "d"])

    def test_solve_text(self):
        self.assertEqual(solve("1 2 4 / 1 3 4"), [1, 1, 2, 3, 4, 4])
        self.assertEqual(solve("1 2 4\n1 3 4", merge_without_dummy), [1, 1, 2, 3, 4, 4])

    def test_big(self):
        n = 100_000
        values_a = list(range(0, n, 2))
        values_b = list(range(1, n, 2))
        for merge in MERGES:
            merged = merge(from_list(values_a), from_list(values_b))
            self.assertEqual(to_list(merged), list(range(n)))

    def test_against_sorted(self):
        random.seed(0)
        for _ in range(200):
            n_a, n_b = random.randint(0, 8), random.randint(0, 8)
            values_a = sorted(random.randint(-20, 20) for _ in range(n_a))
            values_b = sorted(random.randint(-20, 20) for _ in range(n_b))
            self.check(values_a, values_b, sorted(values_a + values_b))

    def test_stability(self):
        for merge in MERGES:
            a_nodes, b_nodes = [Node(1), Node(1)], [Node(1), Node(1)]
            a_nodes[0].next, b_nodes[0].next = a_nodes[1], b_nodes[1]
            merged = merge(a_nodes[0], b_nodes[0])
            self.assertEqual(nodes_of(merged), a_nodes + b_nodes, merge.__name__)


if __name__ == "__main__":
    unittest.main(verbosity=2)
