import sys


def do(x):
    for i in range(1, int(x)+1):
        yield '{} Abracadabra'.format(i)


def main(fd):
    for line in fd:
        for result in do(line.strip()):
            print(result)


if __name__ == '__main__':
    main(sys.stdin)
