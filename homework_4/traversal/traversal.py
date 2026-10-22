"""Задача 1. Tree traversal"""

import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.value})"


class BST:
    def __init__(self, values=()):
        self.root = None
        self.size = 0
        for value in values:
            self.insert(value)

    def __len__(self) -> int:
        return self.size

    def insert(self, value) -> Node:
        node = Node(value)
        self.size += 1
        if self.root is None:
            self.root = node
            return node

        parent = self.root
        while True:
            # равные уходят вправо, повторы сохраняются
            if value < parent.value:
                if parent.left is None:
                    parent.left = node
                    return node
                parent = parent.left
            else:
                if parent.right is None:
                    parent.right = node
                    return node
                parent = parent.right


# порядок обхода: N - сам узел, L - левое поддерево, R - правое
PREORDER, INORDER, POSTORDER = "NLR", "LNR", "LRN"
REVERSE_PREORDER, REVERSE_INORDER, REVERSE_POSTORDER = "NRL", "RNL", "RLN"


def traverse(root: Node | None, order: str) -> list:
    """Обход в глубину своим стеком, порядок задан строкой из N, L, R"""
    result = []
    stack = (
        [(root, False)] if root is not None else []
    )  # (узел, пора ли выдать значение)
    while stack:
        node, emit = stack.pop()
        if emit:
            result.append(node.value)
            continue
        # кладем задом наперед, чтобы первым сняли order[0]
        for part in reversed(order):
            if part == "N":
                stack.append((node, True))
            elif part == "L" and node.left is not None:
                stack.append((node.left, False))
            elif part == "R" and node.right is not None:
                stack.append((node.right, False))
    return result


def preorder(root: Node | None) -> list:
    return traverse(root, PREORDER)


def inorder(root: Node | None) -> list:
    return traverse(root, INORDER)


def postorder(root: Node | None) -> list:
    return traverse(root, POSTORDER)


def reverse_preorder(root: Node | None) -> list:
    return traverse(root, REVERSE_PREORDER)


def reverse_inorder(root: Node | None) -> list:
    return traverse(root, REVERSE_INORDER)


def reverse_postorder(root: Node | None) -> list:
    return traverse(root, REVERSE_POSTORDER)


TRAVERSALS = [
    ("preorder", preorder),
    ("inorder", inorder),
    ("postorder", postorder),
    ("reverse preorder", reverse_preorder),
    ("reverse inorder", reverse_inorder),
    ("reverse postorder", reverse_postorder),
]


def parse(text: str) -> list[int]:
    return [int(x) for x in text.split()]


def solve(text: str) -> str:
    root = BST(parse(text)).root
    width = max(len(name) for name, _ in TRAVERSALS)
    return "\n".join(
        f"{name + ':':<{width + 1}} {' '.join(map(str, walk(root)))}".rstrip()
        for name, walk in TRAVERSALS
    )


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


def trace(values: list[int]) -> None:
    print(f"вставляем: {' '.join(map(str, values))}")
    print()
    head = f"{'шаг':>4} | {'значение':>8} | {'путь от корня':<24} | куда"
    print(head)
    print("-" * (len(head) + 16))

    tree = BST()
    for step, value in enumerate(values, 1):
        path, parent, side = [], tree.root, "корень"
        while parent is not None:
            path.append(str(parent.value))
            side = "влево" if value < parent.value else "вправо"
            nxt = parent.left if value < parent.value else parent.right
            if nxt is None:
                side = f"{side} от {parent.value}"
            parent = nxt
        tree.insert(value)
        route = " -> ".join(path) or "-"
        print(f"{step:>4} | {str(value):>8} | {route:<24} | {side}")

    print()
    for line in draw(tree.root):
        print("    " + line)

    print()
    order = INORDER
    print(f"обход inorder ({order}) по шагам,", end=" ")
    print("[x] - выдать значение, x - раскрыть узел:")
    print()
    head = (
        f"{'шаг':>4} | {'снимаем':<8} | {'кладем':<16}"
        f" | {'стек (дно -> вершина)':<36} | результат"
    )
    print(head)
    print("-" * (len(head) + 10))

    def label(item: tuple) -> str:
        node, emit = item
        return f"[{node.value}]" if emit else str(node.value)

    result, step = [], 0
    stack = [(tree.root, False)] if tree.root is not None else []
    while stack:
        step += 1
        item = stack.pop()
        node, emit = item
        pushed = []
        if emit:
            result.append(node.value)
        else:
            for part in reversed(order):
                if part == "N":
                    pushed.append((node, True))
                elif part == "L" and node.left is not None:
                    pushed.append((node.left, False))
                elif part == "R" and node.right is not None:
                    pushed.append((node.right, False))
            stack += pushed
        added = " ".join(map(label, pushed))
        waiting = " ".join(map(label, stack))
        out = " ".join(map(str, result))
        print(
            (
                f"{step:>4} | {label(item):<8} | {added:<16}"
                f" | {waiting:<36} | {out}"
            ).rstrip()
        )

    print()
    print("все шесть обходов:")
    for line in solve(" ".join(map(str, values))).splitlines():
        print("  " + line)


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(parse(" ".join(argv[1:]) or "6 2 7 1 4 9 3 5 8"))
        return
    print(solve(" ".join(argv) if argv else sys.stdin.read()))


if __name__ == "__main__":
    main(sys.argv[1:])
