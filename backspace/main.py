import re
import sys


def backspace(fd):
    line = fd.read().strip()
    while '<' in line:
        line = re.sub('\w<', '', line)
    return line


def main(fd):
    print(backspace(fd))


if __name__ == '__main__':
    main(sys.stdin)
