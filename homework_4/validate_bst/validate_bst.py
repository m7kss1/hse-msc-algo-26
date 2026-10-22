"""Задача 2. Validate BST"""

import sys
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.value})"


def is_valid_bst(root: Node | None) -> bool:
    """Каждый узел строго внутри границ, заданных предками"""
    # (узел, нижняя граница, верхняя граница), None - границы нет
    stack = [(root, None, None)] if root is not None else []
    while stack:
        node, low, high = stack.pop()
        if (low is not None and node.value <= low) or (
            high is not None and node.value >= high
        ):
            return False
        # левого кладем последним, чтобы снять первым
        if node.right is not None:
            stack.append((node.right, node.value, high))
        if node.left is not None:
            stack.append((node.left, low, node.value))
    return True


def parse(text: str) -> Node | None:
    """Дерево в порядке обхода по уровням, пустой узел - null"""
    for ch in ",[]":
        text = text.replace(ch, " ")
    values = [None if t in ("null", "None") else int(t) for t in text.split()]
    return from_level_order(values)


def from_level_order(values: list) -> Node | None:
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue = deque([root])  # узлы, которым ещё не раздали детей
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


def solve(text: str) -> bool:
    return is_valid_bst(parse(text))


def draw(root: Node | None) -> list[str]:
    def build(node: Node) -> tuple[list[str], int, int]:
        label = str(node.value)
        u = len(label)
        if node.left is None and node.right is None:
            return [label], u, u // 2

        if node.left is not None:
            left, n, x = build(node.left)
        else:
            left, n, x = [], 0, 0
        if node.right is not None:
            right, m, y = build(node.right)
        else:
            right, m, y = [], 0, 0

        first = ""
        second = ""
        if node.left is not None:
            first += " " * (x + 1) + "_" * (n - x - 1)
            second += " " * x + "/" + " " * (n - x - 1)
        first += label
        second += " " * u
        if node.right is not None:
            first += "_" * y + " " * (m - y)
            second += " " * y + "\\" + " " * (m - y - 1)

        height = max(len(left), len(right))
        left += [" " * n] * (height - len(left))
        right += [" " * m] * (height - len(right))
        lines = [first, second] + [
            a + " " * u + b for a, b in zip(left, right)
        ]
        return lines, n + u + m, n + u // 2

    if root is None:
        return ["(пустое дерево)"]
    return [line.rstrip() for line in build(root)[0]]


def trace(root: Node | None) -> None:
    for line in draw(root):
        print("    " + line)
    print()
    head = (
        f"{'шаг':>4} | {'узел':>6} | {'допустимо':<16} | {'проверка':<8}"
        f" | стек (дно -> вершина)"
    )
    print(head)
    print("-" * (len(head) + 10))

    def bound(value, default: str) -> str:
        return default if value is None else str(value)

    def interval(low, high) -> str:
        return f"({bound(low, '-inf')}, {bound(high, '+inf')})"

    stack = [(root, None, None)] if root is not None else []
    step = 0
    while stack:
        step += 1
        node, low, high = stack.pop()
        ok = not (
            (low is not None and node.value <= low)
            or (high is not None and node.value >= high)
        )
        if ok:
            if node.right is not None:
                stack.append((node.right, node.value, high))
            if node.left is not None:
                stack.append((node.left, low, node.value))
        pending = " ".join(
            f"{n.value}{interval(lo, hi)}" for n, lo, hi in stack
        )
        print(
            (
                f"{step:>4} | {str(node.value):>6} | {interval(low, high):<16}"
                f" | {'ok' if ok else 'НАРУШЕНО':<8} | {pending}"
            ).rstrip()
        )
        if not ok:
            print(
                f"\n{node.value} не лежит в {interval(low, high)}  ->  False"
            )
            return
    print("\nвсе узлы внутри своих границ  ->  True")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(parse(" ".join(argv[1:]) or "8 3 10 1 6 null 14 null null 4 9"))
        return
    print(solve(" ".join(argv) if argv else sys.stdin.read()))


if __name__ == "__main__":
    main(sys.argv[1:])
