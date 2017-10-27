import sys


def do(x):
    for i in range(1, int(x)+1):
        yield '{} Abracadabra'.format(i)


def main(fd):
    for line in fd:
        for result in do(line.strip()):
            print(result)


main(sys.stdin)
