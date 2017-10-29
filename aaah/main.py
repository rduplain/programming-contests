import sys


def how_long(ah):
    return len(ah.rstrip('h'))


def aaah(fd):
    able = fd.readline().strip()
    required = fd.readline().strip()
    if how_long(able) >= how_long(required):
        return 'go'
    else:
        return 'no'


def main(fd):
    print(aaah(fd))


if __name__ == '__main__':
    main(sys.stdin)
