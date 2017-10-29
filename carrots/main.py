import sys


def carrots(fd):
    n, p = fd.readline().strip().split(' ')
    n, p = int(n), int(p)
    return p


def main(fd):
    print(carrots(fd))


if __name__ == '__main__':
    main(sys.stdin)
