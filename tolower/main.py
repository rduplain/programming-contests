import sys


def read_n_lines(fd, n):
    return [fd.readline().strip() for i in range(n)]


def foo(fd, p, t):
    for line in read_n_lines(fd, t):
        if not line[1:].islower():
            return False
    return True


def tolower(fd):
    p, t = fd.readline().strip().split(' ')
    p, t = int(p), int(t)
    count = 0
    for x in range(p):
        if foo(fd, p, t):
            count += 1
    print(count)


def main(fd):
    tolower(fd)


if __name__ == '__main__':
    main(sys.stdin)
