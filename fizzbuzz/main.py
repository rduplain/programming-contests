import sys


def fizzbuzz_of(i, x, y, fizz='Fizz', buzz='Buzz'):
    "Fizz on x, Buzz on y."
    if (i % x == 0) and (i % y == 0):
        return ''.join((fizz, buzz))
    elif i % x == 0:
        return fizz
    elif i % y == 0:
        return buzz
    else:
        return str(i)


def fizzbuzz(fd):
    x, y, n = fd.readline().strip().split(' ')
    x, y, n = int(x), int(y), int(n)
    for i in range(1, n+1):
        print(fizzbuzz_of(i, x, y))


def main(fd):
    fizzbuzz(fd)


if __name__ == '__main__':
    main(sys.stdin)
