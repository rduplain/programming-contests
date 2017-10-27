import sys


def do(x):
    return int(x) % 42


def main(fd):
    unique = set(do(line.strip()) for line in fd)
    print(len(unique))


main(sys.stdin)
