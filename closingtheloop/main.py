import sys


def reverse_sorted(*a):
    "Improve readability when using generators."
    return sorted(*a, reverse=True)


def closingtheloop(fd):
    s = int(fd.readline().strip())
    xs = fd.readline().strip().split(' ')
    r = reverse_sorted(int(x.rstrip('R')) for x in xs if x.endswith('R'))
    b = reverse_sorted(int(x.rstrip('B')) for x in xs if x.endswith('B'))
    # Subtract 1cm for each segment, to account for knots.
    return sum(ri + bi - 2 for ri, bi in zip(r, b))


def main(fd):
    count = int(fd.readline())
    for i in range(1, count+1):
        print('Case #{}: {}'.format(i, closingtheloop(fd)))


if __name__ == '__main__':
    main(sys.stdin)
