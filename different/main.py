import sys


def different(fd):
    for line in fd:
        x, y = line.strip().split(' ')
        x, y = int(x), int(y)
        yield abs(x - y)


def main(fd):
    for result in different(fd):
        print(result)


if __name__ == '__main__':
    main(sys.stdin)
