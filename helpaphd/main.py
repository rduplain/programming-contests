import sys


def helpaphd(line):
    parts = line.split('+')
    if len(parts) < 2:
        return 'skipped'
    x, y = parts
    x, y = int(x), int(y)
    return x + y


def main(fd):
    _ = fd.readline()
    for line in fd:
        print(helpaphd(line.strip()))


if __name__ == '__main__':
    main(sys.stdin)
