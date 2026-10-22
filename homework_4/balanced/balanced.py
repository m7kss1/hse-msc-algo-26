"""Задача 3. Balanced binary tree"""

import sys
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.value})"


def is_balanced(root: Node | None) -> bool:
    """Обход снизу вверх (postorder): высота узла считается из высот детей"""
    heights = []  # высоты готовых поддеревьев, тоже стек
    stack = [(root, False)]  # (узел, дети уже посчитаны)
    while stack:
        node, done = stack.pop()
        if node is None:
            heights.append(0)  # высота пустого поддерева
        elif not done:
            # сначала левое, потом правое, потом сам узел
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            right, left = heights.pop(), heights.pop()
            if abs(left - right) > 1:
                return False  # дальше считать незачем
            heights.append(max(left, right) + 1)
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
    return is_balanced(parse(text))


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
        f"{'шаг':>4} | {'узел':>6} | {'h(лев)':>6} | {'h(прав)':>7}"
        f" | {'разница':>7} | {'h(узла)':>7} | стек высот"
    )
    print(head)
    print("-" * (len(head) + 6))

    heights, step = [], 0
    stack = [(root, False)]
    while stack:
        node, done = stack.pop()
        if node is None:
            heights.append(0)
        elif not done:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            step += 1
            right, left = heights.pop(), heights.pop()
            diff = abs(left - right)
            ok = diff <= 1
            if ok:
                heights.append(max(left, right) + 1)
            mark = f"{max(left, right) + 1:>7}" if ok else f"{'-':>7}"
            print(
                f"{step:>4} | {str(node.value):>6} | {left:>6} | {right:>7}"
                f" | {diff:>7} | {mark} | {heights}"
            )
            if not ok:
                print(
                    f"\nу узла {node.value} высоты {left} и {right},", end=" "
                )
                print(f"разница {diff} > 1  ->  False")
                return
    print(f"\nвысота дерева {heights[0]},", end=" ")
    print("у всех узлов разница не больше 1  ->  True")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        text = " ".join(argv[1:]) or "1 2 3 4 5 null 6 7 null null null null 8"
        trace(parse(text))
        return
    print(solve(" ".join(argv) if argv else sys.stdin.read()))


if __name__ == "__main__":
    main(sys.argv[1:])
