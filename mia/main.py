import sys


def rank(x0, x1):
    if (x0 == 1 and x1 == 2) or (x0 == 2 and x1 == 1):
        return 1000
    if x0 == x1:
        return 100 + x0*10 + x1
    if x1 > x0:
        return x1*10 + x0
    return x0*10 + x1


def mia(line):
    s0, s1, r0, r1 = line.split(' ')
    s0, s1, r0, r1 = int(s0), int(s1), int(r0), int(r1)

    player1 = rank(s0, s1)
    player2 = rank(r0, r1)

    if player1 > player2:
        return "Player 1 wins."
    elif player2 > player1:
        return "Player 2 wins."
    return "Tie."


def main(fd):
    for line in fd:
        line = line.strip()
        if line == '0 0 0 0':
            break
        print(mia(line))


if __name__ == '__main__':
    main(sys.stdin)
