import sys


def hello(fd):
    return 'Hello World!'


def main(fd):
    print(hello(fd))


if __name__ == '__main__':
    main(sys.stdin)
