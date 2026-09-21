"""Задача 1. Stack vs queue"""

import sys


class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """LIFO: кладем и снимаем с вершины, вершина - голова списка"""

    def __init__(self, items=()):
        self._head = None
        self._size = 0
        for item in items:
            self.push(item)

    def push(self, value) -> None:
        self._head = _Node(value, self._head)
        self._size += 1

    def pop(self):
        node = self._head
        if node is None:
            raise IndexError("стек пуст")
        self._head = node.next
        self._size -= 1
        return node.value

    def peek(self):
        if self._head is None:
            raise IndexError("стек пуст")
        return self._head.value

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value
            node = node.next

    def __repr__(self) -> str:
        return f"Stack({list(self)})"


class Queue:
    """FIFO: добавляем в хвост, снимаем с головы, поэтому храним обе ссылки"""

    def __init__(self, items=()):
        self._head = None
        self._tail = None
        self._size = 0
        for item in items:
            self.enqueue(item)

    def enqueue(self, value) -> None:
        node = _Node(value)
        if self._tail is None:  # очередь была пуста, узел сразу и голова, и хвост
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        node = self._head
        if node is None:
            raise IndexError("очередь пуста")
        self._head = node.next
        if self._head is None:  # сняли последний, хвост тоже сбрасываем
            self._tail = None
        self._size -= 1
        return node.value

    def peek(self):
        if self._head is None:
            raise IndexError("очередь пуста")
        return self._head.value

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value
            node = node.next

    def __repr__(self) -> str:
        return f"Queue({list(self)})"


def trace(items: list) -> None:
    stack, queue = Stack(), Queue()
    head = (
        f"{'шаг':>4} | {'операция':<11} | {'стек (вершина -> дно)':<25}"
        f" | {'очередь (голова -> хвост)':<25}"
    )
    print(head.rstrip())
    print("-" * len(head))

    def show(step: int, op: str, from_stack: str = "", from_queue: str = "") -> None:
        left = "[" + ", ".join(map(str, stack)) + "]" + from_stack
        right = "[" + ", ".join(map(str, queue)) + "]" + from_queue
        print(f"{step:>4} | {op:<11} | {left:<25} | {right:<25}".rstrip())

    show(0, "-")
    step = 0
    for item in items:
        step += 1
        stack.push(item)
        queue.enqueue(item)
        show(step, f"добавили {item}")

    taken_stack, taken_queue = [], []
    while stack:
        step += 1
        taken_stack.append(stack.pop())
        taken_queue.append(queue.dequeue())
        show(step, "сняли", f" -> {taken_stack[-1]}", f" -> {taken_queue[-1]}")

    print()
    print(f"стек выдал:     {' '.join(map(str, taken_stack))}  (LIFO)")
    print(f"очередь выдала: {' '.join(map(str, taken_queue))}  (FIFO)")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(argv[1:] or [1, 2, 3])
        return
    items = (" ".join(argv) if argv else sys.stdin.read()).split()
    stack, queue = Stack(items), Queue(items)
    print(f"{'стек:':<9}" + " ".join(stack.pop() for _ in range(len(stack))))
    print(f"{'очередь:':<9}" + " ".join(queue.dequeue() for _ in range(len(queue))))


if __name__ == "__main__":
    main(sys.argv[1:])
