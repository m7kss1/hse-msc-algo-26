"""Задача 2. Anagrams"""

import json
import sys


def signature(word: str) -> str:
    """Буквы слова по порядку: у анаграмм и только у них она совпадает"""
    return "".join(sorted(word))


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}  # подпись -> слова с этой подписью
    for word in words:
        groups.setdefault(signature(word), []).append(word)
    return list(groups.values())


def canonical(groups: list[list[str]]) -> list[list[str]]:
    """Порядок как в примере из условия: слова в группе по алфавиту, группы по размеру"""
    return sorted((sorted(group) for group in groups), key=lambda g: (len(g), g))


def to_json(groups: list[list[str]]) -> str:
    return json.dumps(groups, ensure_ascii=False, separators=(",", ":"))


def solve(text: str) -> str:
    return to_json(canonical(group_anagrams(text.split())))


def trace(words: list[str]) -> None:
    print(f"strs = {words}")
    print()
    head = f"{'шаг':>4} | {'слово':<8} | {'подпись':<8} | группа после шага"
    print(head)
    print("-" * (len(head) + 8))

    groups = {}
    for step, word in enumerate(words, 1):
        key = signature(word)
        new = key not in groups
        groups.setdefault(key, []).append(word)
        group = ("новая: " if new else "") + "[" + ", ".join(groups[key]) + "]"
        print(f"{step:>4} | {word:<8} | {key:<8} | {group}")

    print()
    print("группы:")
    for key, group in groups.items():
        print(f"  {key:<8} -> {group}")
    print(f"\nответ: {to_json(canonical(list(groups.values())))}")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(argv[1:] or ["eat", "tea", "tan", "ate", "nat", "bat"])
        return
    print(solve(" ".join(argv) if argv else sys.stdin.read()))


if __name__ == "__main__":
    main(sys.argv[1:])
