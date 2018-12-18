import sys


def helpaphd(line):
    try:
        x, y = line.split('+')
    except ValueError:
        return 'skipped'
    return int(x) + int(y)


def main(fd):
    _ = fd.readline()
    for line in fd:
        print(helpaphd(line.strip()))


if __name__ == '__main__':
    main(sys.stdin)
