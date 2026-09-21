import random
import unittest

from validate import solve, validate


def brute_force(pushed: list, popped: list) -> bool:
    """Полный перебор: на каждом шаге либо push следующего, либо pop вершины"""
    n = len(pushed)
    seen = set()

    def search(i: int, done: int, stack: tuple) -> bool:
        if done == n:
            return True
        if (i, done, stack) in seen:
            return False
        seen.add((i, done, stack))
        if stack and stack[-1] == popped[done] and search(i, done + 1, stack[:-1]):
            return True
        return i < n and search(i + 1, done, stack + (pushed[i],))

    return len(pushed) == len(popped) and search(0, 0, ())


class TestValidate(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]))
        self.assertFalse(validate([1, 2, 3], [3, 1, 2]))

    def test_one_element(self):
        self.assertTrue(validate([1], [1]))

    def test_same_order(self):
        """push/pop сразу после каждого push"""
        self.assertTrue(validate([1, 2, 3, 4], [1, 2, 3, 4]))

    def test_reversed_order(self):
        """сначала все push, потом все pop"""
        self.assertTrue(validate([1, 2, 3, 4], [4, 3, 2, 1]))

    def test_impossible(self):
        self.assertFalse(validate([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
        self.assertFalse(validate([1, 2, 3, 4], [2, 4, 1, 3]))

    def test_not_a_permutation(self):
        """условие такого не обещает, но падать программа не должна"""
        self.assertFalse(validate([1, 2, 3], [1, 2, 4]))
        self.assertFalse(validate([1, 2, 3], [1, 2]))
        self.assertFalse(validate([], [1]))

    def test_empty(self):
        self.assertTrue(validate([], []))

    def test_duplicates_are_out_of_scope(self):
        """На повторах жадность ломается, поэтому условие и требует уникальности

        Контрпример: pushed = 0 1 0 0 2 2, popped = 0 0 2 1 2 0. Схема есть:
        push 0 1 0 0, pop, pop, push 2, pop, pop, push 2, pop, pop.
        Жадность снимает самый первый 0 сразу и заходит в тупик
        """
        pushed, popped = [0, 1, 0, 0, 2, 2], [0, 0, 2, 1, 2, 0]
        self.assertTrue(brute_force(pushed, popped))
        self.assertFalse(validate(pushed, popped))

    def test_strings(self):
        self.assertTrue(validate(["a", "b"], ["b", "a"]))

    def test_solve_text(self):
        self.assertTrue(solve("1 2 3 4 5 / 1 3 5 4 2"))
        self.assertFalse(solve("1 2 3\n3 1 2"))

    def test_big(self):
        n = 100_000
        pushed = list(range(n))
        self.assertTrue(validate(pushed, pushed))
        self.assertTrue(validate(pushed, pushed[::-1]))
        self.assertFalse(validate(pushed, pushed[-1:] + pushed[:-1]))

    def test_against_brute_force(self):
        random.seed(0)
        for _ in range(300):
            n = random.randint(0, 7)
            pushed = list(range(n))
            popped = pushed[:]
            random.shuffle(popped)
            self.assertEqual(
                validate(pushed, popped), brute_force(pushed, popped), (pushed, popped)
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
