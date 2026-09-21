"""Задача 2. Validate"""

import sys


def validate(pushed: list, popped: list) -> bool:
    """Могут ли pushed и popped получиться операциями push/pop над пустым стеком"""
    if len(pushed) != len(popped):
        return False

    stack = []
    done = 0  # сколько элементов popped уже выдано
    for value in pushed:
        stack.append(value)
        # вершина совпала с ожидаемым - снимаем сразу, иначе мы её закопаем
        while stack and stack[-1] == popped[done]:
            stack.pop()
            done += 1

    return not stack  # стек пуст, значит выдали ровно popped


def solve(text: str) -> bool:
    """Тот же ответ, но по тексту вида '1 2 3 4 5 / 1 3 5 4 2'"""
    pushed, popped = parse(text)
    return validate(pushed, popped)


def parse(text: str) -> tuple[list[int], list[int]]:
    """Две последовательности, разделенные '/' или переводом строки"""
    parts = [p for p in text.replace("\n", "/").split("/") if p.strip()]
    if len(parts) != 2:
        raise ValueError("нужны две последовательности, разделенные '/'")
    return tuple([int(x) for x in p.split()] for p in parts)


def trace(pushed: list, popped: list) -> None:
    """Печатает пошаговое состояние стека"""
    print(f"pushed: {' '.join(map(str, pushed))}")
    print(f"popped: {' '.join(map(str, popped))}")
    print()
    head = (
        f"{'шаг':>4} | {'действие':<8} | {'стек (дно -> вершина)':<24}"
        f" | {'ждем':>5} | {'выдано':<20}"
    )
    print(head.rstrip())
    print("-" * len(head))

    stack, out, done, step = [], [], 0, 0

    def show(action: str) -> None:
        wait = popped[done] if done < len(popped) else "-"
        print(
            (
                f"{step:>4} | {action:<8} | {str(stack):<24}"
                f" | {wait:>5} | {' '.join(map(str, out))}"
            ).rstrip()
        )

    for value in pushed:
        step += 1
        stack.append(value)
        show(f"push {value}")
        while stack and done < len(popped) and stack[-1] == popped[done]:
            step += 1
            out.append(stack.pop())
            done += 1
            show(f"pop {out[-1]}")

    print()
    if stack:
        print(f"стек не опустел, осталось {stack}  ->  False")
    else:
        print("стек пуст, выдали ровно popped  ->  True")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        text = " ".join(argv[1:]) or "1 2 3 4 5 / 1 3 5 4 2"
        trace(*parse(text))
        return
    print(solve(" ".join(argv) if argv else sys.stdin.read()))


if __name__ == "__main__":
    main(sys.argv[1:])
