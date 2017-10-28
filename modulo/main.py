import sys


def do(x):
    return int(x) % 42


def main(fd):
    unique = set(do(line.strip()) for line in fd)
    print(len(unique))


if __name__ == '__main__':
    main(sys.stdin)
