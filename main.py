# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    brackets_map = {"(": ")", "{": "}", "[": "]"}
    for i, char in enumerate(text):
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or brackets_map[stack.pop()] != char:
                return i + 1
    if stack:
        return len(text) + 1
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
