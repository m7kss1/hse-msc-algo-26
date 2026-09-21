"""Задача 3. Merge lists"""

import sys


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value})"


def merge_with_dummy(a: Node | None, b: Node | None) -> Node | None:
    dummy = Node(None)
    tail = dummy
    while a is not None and b is not None:
        if a.value <= b.value:  # <= чтобы равные элементы шли в порядке a, b
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a if a is not None else b  # остаток уже отсортирован, цепляем целиком
    return dummy.next


def merge_without_dummy(a: Node | None, b: Node | None) -> Node | None:
    if a is None:
        return b
    if b is None:
        return a

    if b.value < a.value:  # голова результата - меньший из первых элементов
        a, b = b, a
    head = tail = a
    a = a.next

    while a is not None and b is not None:
        if a.value <= b.value:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return head


def from_list(values) -> Node | None:
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def to_list(head: Node | None) -> list:
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next
    return values


def solve(text: str, merge=merge_with_dummy) -> list:
    values_a, values_b = parse(text)
    return to_list(merge(from_list(values_a), from_list(values_b)))


def parse(text: str) -> tuple[list[int], list[int]]:
    """Два списка, разделенные '/' или переводом строки"""
    parts = [p for p in text.replace("\n", "/").split("/") if p.strip()]
    if len(parts) != 2:
        raise ValueError("нужны два списка, разделенные '/'")
    return tuple([int(x) for x in p.split()] for p in parts)


def trace(values_a: list, values_b: list) -> None:
    print(f"list1 = {values_a}")
    print(f"list2 = {values_b}")
    print()
    head = (
        f"{'шаг':>4} | {'сравнение':<12} | {'берем':<7} | {'результат':<24}"
        f" | {'остаток list1':<15} | {'остаток list2':<15}"
    )
    print(head.rstrip())
    print("-" * len(head))

    a, b = from_list(values_a), from_list(values_b)
    result, step = [], 0

    def show(compare: str, taken: str) -> None:
        print(
            (
                f"{step:>4} | {compare:<12} | {taken:<7} | {str(result):<24}"
                f" | {str(to_list(a)):<15} | {str(to_list(b))}"
            ).rstrip()
        )

    show("-", "-")
    while a is not None and b is not None:
        step += 1
        if a.value <= b.value:
            compare, taken, value = f"{a.value} <= {b.value}", "list1", a.value
            a = a.next
        else:
            compare, taken, value = f"{b.value} <  {a.value}", "list2", b.value
            b = b.next
        result.append(value)
        show(compare, taken)

    step += 1
    taken = "list1" if a is not None else "list2" if b is not None else "-"
    result += to_list(a if a is not None else b)
    a = b = None  # хвост целиком уехал в результат
    show("один пуст", taken)
    print(f"\nответ: {result}")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(*parse(" ".join(argv[1:]) or "1 2 4 8 / 1 3 4"))
        return
    text = " ".join(argv) if argv else sys.stdin.read()
    for label, merge in [
        ("с фиктивным узлом:", merge_with_dummy),
        ("без фиктивного:", merge_without_dummy),
    ]:
        print(f"{label:<20}" + " ".join(map(str, solve(text, merge))))


if __name__ == "__main__":
    main(sys.argv[1:])
