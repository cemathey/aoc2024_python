import sys


def load_lines():
    lines: list[list[int]] = []
    with open(sys.argv[1]) as fp:
        for line in fp.readlines():
            lines.append([int(num) for num in line.split()])

    print(f"{len(lines)=}")
    return lines


def main():
    lines = load_lines()
    total = sum(1 for level in lines if is_safe(level))
    print(f"Part 1 {total=}")


def is_safe(level: list[int], min_dist=1, max_dist=3) -> bool:
    deltas: list[int] = []
    for n1, n2 in zip(level, level[1:]):
        deltas.append(n1 - n2)

    first_delta = None
    for d in deltas:
        if not first_delta:
            first_delta = d

        if not min_dist <= abs(d) <= max_dist:
            return False

        if first_delta < 0 and d > 0:
            return False

        if first_delta > 0 and d < 0:
            return False

    return True


if __name__ == "__main__":
    main()

    assert is_safe([7, 6, 4, 2, 1])
    assert not is_safe([1, 2, 7, 8, 9])
    assert not is_safe([9, 7, 6, 2, 1])
    assert not is_safe([1, 3, 2, 4, 5])
    assert not is_safe([8, 6, 4, 4, 1])
    assert is_safe([1, 3, 6, 7, 9])
    assert is_safe([])
