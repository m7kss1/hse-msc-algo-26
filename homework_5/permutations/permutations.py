"""Задача 2. Permutations"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tracer"))
from tracer import tracer


def permutations(nums, trace=False):
    """Вернуть перестановки позиций; одинаковые значения могут повторяться"""
    result = []
    used = [False] * len(nums)  # какие позиции уже есть в пути
    path = []

    def visit():
        if len(path) == len(nums):
            result.append(path.copy())  # дальше path будет меняться
            return
        for i, value in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(value)
                visit_call()
                path.pop()  # отменяем выбор перед следующей веткой
                used[i] = False

    # передаем снимок пути, чтобы его было видно при каждом входе в стек
    def step(current):
        visit()
        return current

    def visit_call():
        return traced_step(path.copy())

    traced_step = tracer(step) if trace else step
    visit_call()
    return result


def main(argv):
    trace = bool(argv and argv[0] == "--trace")
    if trace:
        argv = argv[1:]
    text = " ".join(argv) if argv else sys.stdin.read()
    for ch in "[],":
        text = text.replace(ch, " ")
    print(permutations([int(x) for x in text.split()], trace=trace))


if __name__ == "__main__":
    main(sys.argv[1:])
