import string
import random
import sys


def generate(width, p=0.1):
    for _ in range(width):
        if random.random() < p:
            yield '<'
        else:
            yield random.choice(string.ascii_lowercase)


def main(argv):
    try:
        width = int(argv[1])
    except IndexError:
        width = 10**6
    print(''.join(generate(width)))


if __name__ == '__main__':
    main(sys.argv)
