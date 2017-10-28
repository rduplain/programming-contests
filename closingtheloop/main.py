import sys


def rsorted(*a):
    "Improve readability when using generators."
    return sorted(*a, reverse=True)


def rope(fd):
    s = int(fd.readline().strip())
    xs = fd.readline().strip().split(' ')
    return sum(
        # Subtract 1cm for each segment.
        ri + bi - 2 for ri, bi
        in zip(rsorted(int(x.rstrip('R')) for x in xs if x.endswith('R')),
               rsorted(int(x.rstrip('B')) for x in xs if x.endswith('B'))))


def main(fd):
    count = int(fd.readline())
    for i in range(1, count+1):
        print('Case #{}: {}'.format(i, rope(fd)))


main(sys.stdin)
