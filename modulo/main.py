import sys


def modulo(x):
    return int(x) % 42


def main(fd):
    unique = set(modulo(line.strip()) for line in fd)
    print(len(unique))


if __name__ == '__main__':
    main(sys.stdin)
