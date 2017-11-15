import sys


def anotherbrick(fd):
    h, w, n = fd.readline().strip().split(' ')
    h, w, n = int(h), int(w), int(n)
    brick = list(map(int, fd.readline().strip().split(' ')))

    try:
        for _ in range(h):
            remaining = w
            while remaining > 0:
                remaining -= brick.pop(0)
            if remaining < 0:
                return False
    except IndexError:
        return False
    return True


def main(fd):
    if anotherbrick(fd):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main(sys.stdin)
