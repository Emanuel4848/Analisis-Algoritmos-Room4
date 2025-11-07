from typing import List, Iterable, TypeVar
import random
import time

T = TypeVar("T")


def bubble_sort(a: List[T], *, reverse: bool = False) -> None:
    n = len(a)
    if n < 2:
        return

    def goes_before(x: T, y: T) -> bool:
        return (x > y) if not reverse else (x < y)

    last_unsorted = n - 1
    while last_unsorted > 0:
        swapped = False
        new_last_unsorted = 0
        for i in range(last_unsorted):
            if goes_before(a[i], a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                new_last_unsorted = i
        if not swapped:
            break
        last_unsorted = new_last_unsorted


def is_sorted(a: Iterable[T], *, reverse: bool = False) -> bool:
    it = iter(a)
    try:
        prev = next(it)
    except StopIteration:
        return True
    for x in it:
        if (not reverse and prev > x) or (reverse and prev < x):
            return False
        prev = x
    return True


def _benchmark_once(data: List[int], *, reverse: bool = False) -> tuple[float, float]:
    a1 = data[:]
    a2 = data[:]

    t0 = time.perf_counter()
    bubble_sort(a1, reverse=reverse)
    tb = time.perf_counter() - t0

    t0 = time.perf_counter()
    s = sorted(a2, reverse=reverse)
    ts = time.perf_counter() - t0

    assert is_sorted(a1, reverse=reverse)
    assert is_sorted(s, reverse=reverse)
    return tb, ts


def _make_cases(n: int) -> dict[str, List[int]]:
    best = list(range(n))
    avg = best[:]
    random.shuffle(avg)
    worst = list(range(n - 1, -1, -1))
    return {"mejor": best, "promedio": avg, "peor": worst}


def _human(seconds: float) -> str:
    if seconds < 1e-6:
        return f"{seconds*1e9:.1f} ns"
    if seconds < 1e-3:
        return f"{seconds*1e6:.1f} µs"
    if seconds < 1:
        return f"{seconds*1e3:.2f} ms"
    return f"{seconds:.3f} s"


def main() -> None:
    random.seed(42)
    sizes = [100, 1000, 3000]

    print("Comparación: Bubble Sort vs sorted() de Python")
    print("---")
    for n in sizes:
        print(f"\nTamaño n={n}")
        cases = _make_cases(n)
        for nombre, data in cases.items():
            tb, ts = _benchmark_once(data, reverse=False)
            ratio = (tb / ts) if ts > 0 else float("inf")
            print(
                f"  Caso {nombre:<8} | Bubble: {_human(tb):>8} | "
                f"sorted(): {_human(ts):>8} | ratio ≈ {ratio:>8.2f}×"
            )

    print("\nNotas: Bubble Sort es O(n^2) y normalmente mucho más lento que sorted() (Timsort).")


if __name__ == "__main__":
    main()
