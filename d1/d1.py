import sys


def main():
    with open(sys.argv[1]) as fp:
        lines = fp.readlines()

    l1: list[int] = []
    l2: list[int] = []
    for line in lines:
        left, right = line.split()
        l1.append(int(left))
        l2.append(int(right))

    assert len(l1) == len(l2)

    deltas = calc_deltas(l1, l2)

    return sum(d for d in deltas)


def calc_deltas(l1: list[int], l2: list[int]):
    deltas = []
    for n1, n2 in zip(sorted(l1), sorted(l2)):
        deltas.append(abs(n1 - n2))

    return deltas


if __name__ == "__main__":
    deltas = calc_deltas([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    assert sum(d for d in deltas) == 11

    distance = main()
    print(f"{distance=}")
