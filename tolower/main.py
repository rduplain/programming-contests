import sys


def read_n_lines(fd, n):
    return [fd.readline().strip() for i in range(n)]


def tolower(fd, p, t):
    for line in read_n_lines(fd, t):
        if not line[1:].islower():
            return False
    return True


def main(fd):
    p, t = fd.readline().strip().split(' ')
    p, t = int(p), int(t)

    print(sum(tolower(fd, p, t) for x in range(p)))


if __name__ == '__main__':
    main(sys.stdin)
