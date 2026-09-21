import random
import unittest

from stack_vs_queue import Queue, Stack


class TestStack(unittest.TestCase):
    def test_lifo(self):
        stack = Stack([1, 2, 3])
        self.assertEqual([stack.pop(), stack.pop(), stack.pop()], [3, 2, 1])

    def test_empty(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        self.assertFalse(stack)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_peek_does_not_remove(self):
        stack = Stack([1, 2])
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(len(stack), 2)

    def test_len_and_iter(self):
        stack = Stack()
        for x in range(5):
            stack.push(x)
        self.assertEqual(len(stack), 5)
        self.assertEqual(list(stack), [4, 3, 2, 1, 0])

    def test_refill_after_empty(self):
        stack = Stack([1])
        stack.pop()
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 0)

    def test_any_values(self):
        stack = Stack(["a", None, (1, 2)])
        self.assertEqual([stack.pop(), stack.pop(), stack.pop()], [(1, 2), None, "a"])

    def test_big(self):
        n = 100_000
        stack = Stack(range(n))
        self.assertEqual(len(stack), n)
        self.assertEqual([stack.pop() for _ in range(n)], list(reversed(range(n))))


class TestQueue(unittest.TestCase):
    def test_fifo(self):
        queue = Queue([1, 2, 3])
        self.assertEqual([queue.dequeue(), queue.dequeue(), queue.dequeue()], [1, 2, 3])

    def test_empty(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)
        self.assertFalse(queue)
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_peek_does_not_remove(self):
        queue = Queue([1, 2])
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 2)

    def test_len_and_iter(self):
        queue = Queue()
        for x in range(5):
            queue.enqueue(x)
        self.assertEqual(len(queue), 5)
        self.assertEqual(list(queue), [0, 1, 2, 3, 4])

    def test_refill_after_empty(self):
        queue = Queue([1])
        queue.dequeue()
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual([queue.dequeue(), queue.dequeue()], [2, 3])
        self.assertEqual(len(queue), 0)

    def test_any_values(self):
        queue = Queue(["a", None, (1, 2)])
        self.assertEqual(
            [queue.dequeue(), queue.dequeue(), queue.dequeue()], ["a", None, (1, 2)]
        )

    def test_big(self):
        n = 100_000
        queue = Queue(range(n))
        self.assertEqual(len(queue), n)
        self.assertEqual([queue.dequeue() for _ in range(n)], list(range(n)))


class TestAgainstReference(unittest.TestCase):
    def test_stack(self):
        random.seed(0)
        stack, reference = Stack(), []
        for _ in range(2000):
            if reference and random.random() < 0.5:
                self.assertEqual(stack.pop(), reference.pop())
            else:
                value = random.randint(0, 99)
                stack.push(value)
                reference.append(value)
            self.assertEqual(len(stack), len(reference))
            self.assertEqual(list(stack), list(reversed(reference)))

    def test_queue(self):
        random.seed(0)
        queue, reference = Queue(), []
        for _ in range(2000):
            if reference and random.random() < 0.5:
                self.assertEqual(queue.dequeue(), reference.pop(0))
            else:
                value = random.randint(0, 99)
                queue.enqueue(value)
                reference.append(value)
            self.assertEqual(len(queue), len(reference))
            self.assertEqual(list(queue), reference)


if __name__ == "__main__":
    unittest.main(verbosity=2)
