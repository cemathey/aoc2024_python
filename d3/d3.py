import re
import sys


P1_PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"
P2_PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
ENABLE = "do()"
DISABLE = "don't()"


def load_lines() -> str:

    with open(sys.argv[1]) as fp:
        lines = fp.readlines()

    print(f"{len(lines)=}")
    return "".join(lines)


def extract_operands(text: str, pattern: str) -> list[tuple[int, int, bool]]:
    operands: list[tuple[int, int, bool]] = []
    enabled = True
    for match in re.findall(pattern, text):
        if len(match) == 2:
            left, right = match
            operands.append((int(left), int(right), enabled))
        else:
            left, right, do, dont = match

            if do == ENABLE:
                enabled = True
            elif dont == DISABLE:
                enabled = False

            if left and right:
                operands.append((int(left), int(right), enabled))

    return operands


def sum_line(line: list[tuple[int, int, bool]]):
    return sum(left * right for left, right, enabled in line if enabled)


def main():
    memory = load_lines()
    total = sum_line(extract_operands(memory, pattern=P1_PATTERN))
    print(f"Part 1 {total=}")

    total = sum_line(extract_operands(memory, pattern=P2_PATTERN))
    print(f"Part 2 {total=}")


if __name__ == "__main__":
    main()

    test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert extract_operands(test, pattern=P1_PATTERN)[0] == (2, 4, True)
    assert extract_operands(test, pattern=P1_PATTERN)[1] == (5, 5, True)
    assert extract_operands(test, pattern=P1_PATTERN)[2] == (11, 8, True)
    assert extract_operands(test, pattern=P1_PATTERN)[3] == (8, 5, True)

    assert sum_line(extract_operands(test, pattern=P1_PATTERN)) == 161

    test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert extract_operands(test, pattern=P2_PATTERN)[0] == (2, 4, True)
    assert extract_operands(test, pattern=P2_PATTERN)[1] == (5, 5, False)
    assert extract_operands(test, pattern=P2_PATTERN)[2] == (11, 8, False)
    assert extract_operands(test, pattern=P2_PATTERN)[3] == (8, 5, True)
    assert sum_line(extract_operands(test, pattern=P2_PATTERN)) == 48
