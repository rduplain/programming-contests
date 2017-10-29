import sys


def nastyhacks(fd, i):
    r, e, c = fd.readline().strip().split(' ')
    r, e, c = int(r), int(e), int(c)

    with_ad = e - c
    if with_ad > r:
        return 'advertise'
    elif with_ad == r:
        return 'does not matter'
    else:
        return 'do not advertise'


def main(fd):
    count = int(fd.readline())
    for i in range(1, count+1):
        print(nastyhacks(fd, i))


if __name__ == '__main__':
    main(sys.stdin)
