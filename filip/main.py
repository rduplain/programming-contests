import sys


def flip(s):
    return ''.join(reversed(s))


def filip(fd):
    x, y = fd.readline().strip().split(' ')
    x, y = int(flip(x)), int(flip(y))
    return max((x, y))


def main(fd):
    print(filip(fd))


if __name__ == '__main__':
    main(sys.stdin)
