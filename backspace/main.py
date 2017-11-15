import collections
import sys


def edit(line):
    acc = collections.deque()
    for c in line:
        if c != '<':
            acc.append(c)
        else:
            acc.pop()
    return acc


def backspace(fd):
    for c in edit(fd.read().strip()):
        sys.stdout.write(c)
    print('')


def main(fd):
    backspace(fd)


if __name__ == '__main__':
    main(sys.stdin)
