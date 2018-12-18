import sys


def cd_case(fd, n, m):
    jack = set(int(fd.readline()) for _ in range(n))
    acc = 0
    for _ in range(m):
        if int(fd.readline()) in jack:
            acc += 1
    return acc


def cd(fd):
    while True:
        n, m = map(int, fd.readline().split())
        if n == 0 and m == 0:
            break
        yield cd_case(fd, n, m)


def main(fd):
    for result in cd(fd):
        print(result)


if __name__ == '__main__':
    main(sys.stdin)
