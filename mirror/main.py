import sys


def read_n_lines(fd, n):
    return [fd.readline() for i in range(n)]


def mirror(fd, i):
    print('Test {}'.format(i))
    r, c = fd.readline().strip().split(' ')
    r, c = int(r), int(c)
    for line in reversed(read_n_lines(fd, r)):
        print(''.join(reversed(line.strip())))


def main(fd):
    count = int(fd.readline())
    for i in range(1, count+1):
        mirror(fd, i)


main(sys.stdin)
