"""Задача 2. Сумма"""

import sys


def max_even_sum(nums: list[int]) -> int:
    """Максимальная сумма элементов массива, делящаяся на 2"""
    total = sum(x for x in nums if x > 0)
    if total % 2 == 0:
        return total

    # чиним четность: либо убрать минимальное положительное нечетное число,
    # либо добавить отрицательное нечетное число, ближайшее к нулю
    drop = min(x for x in nums if x > 0 and x % 2 != 0)
    add = max((x for x in nums if x < 0 and x % 2 != 0), default=None)
    loss = drop if add is None else min(drop, -add)
    return total - loss


def solve(line: str) -> int:
    """Тот же ответ, но по строке вида '5 7 13 2 14'"""
    return max_even_sum([int(x) for x in line.split()])


def trace(line: str) -> None:
    """Печатает разбор решения по шагам"""
    nums = [int(x) for x in line.split()]
    positives = [x for x in nums if x > 0]
    total = sum(positives)

    print(f"числа:               {nums}")
    print(f"берём положительные: {positives}")
    if total % 2 == 0:
        print(f"их сумма:            {total}  - четная, это и есть ответ")
        return
    print(f"их сумма:            {total}  - нечетная, чиним четность")
    print()

    drop = min(x for x in nums if x > 0 and x % 2 != 0)
    add = max((x for x in nums if x < 0 and x % 2 != 0), default=None)
    print(
        f"A) выбросить наименьшее положительное нечетное {drop}: {total} - {drop} = {total - drop}"
    )
    if add is None:
        print("B) отрицательных нечетных нет, вариант недоступен")
    else:
        print(
            f"B) добавить ближайшее к нулю отрицательное нечетное {add}: {total} + ({add}) = {total + add}"
        )
    print()
    print(f"ответ:               {max_even_sum(nums)}")


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--trace":
        trace(" ".join(argv[1:]) or "5 7 13 2 14 -1 -8")
        return
    print(solve(" ".join(argv) if argv else sys.stdin.read()))


if __name__ == "__main__":
    main(sys.argv[1:])
