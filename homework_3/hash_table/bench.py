import gc
import random
import time

import matplotlib.pyplot as plt

from hash_table import ChainingHashTable

TABLES = [
    ("цепочки", ChainingHashTable, "#2a78d6", "-"),
    ("dict", dict, "#8a8984", "--"),
]


def measure(op: str, cls, keys: list, repeat: int = 3) -> float:
    """Лучшее из repeat время в мс, сборщик мусора выключен"""
    best = float("inf")
    for _ in range(repeat):
        table = cls()
        if op != "вставка":
            for key in keys:
                table[key] = key
        gc.disable()
        start = time.perf_counter()
        if op == "вставка":
            for key in keys:
                table[key] = key
        elif op == "поиск":
            for key in keys:
                table[key]
        else:
            for key in keys:
                del table[key]
        best = min(best, time.perf_counter() - start)
        gc.enable()
    return best * 1000


def plot(ax, op: str, keys: list, sizes: list[int]) -> None:
    for name, cls, color, style in TABLES:
        ms = [measure(op, cls, keys[:n]) for n in sizes]
        x = [n / 1000 for n in sizes]
        ax.plot(x, ms, style, color=color, lw=2, marker="o", ms=4, label=name)
    ax.set_xlabel("N, тыс. ключей")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e6e5e0")
    ax.set_axisbelow(True)


def save(fig, axes, path: str) -> None:
    axes[0].set_ylabel("мс на N операций")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2, frameon=False)
    fig.tight_layout(rect=(0, 0, 1, 0.9))
    fig.savefig(path, dpi=150, bbox_inches="tight")


def main() -> None:
    plt.rcParams.update({"font.size": 9, "axes.edgecolor": "#52514e"})

    sizes = [25_000, 50_000, 100_000, 150_000, 200_000]
    keys = random.Random(0).sample(range(10**12), max(sizes))
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.4), sharey=True)
    for ax, op in zip(axes, ["вставка", "поиск", "удаление"]):
        plot(ax, op, keys, sizes)
        ax.set_title(f"{op}, случайные int")
    save(fig, axes, "latency.png")


if __name__ == "__main__":
    main()
