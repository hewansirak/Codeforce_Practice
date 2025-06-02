import sys

def solve():
    n = int(sys.stdin.readline())
    initstate = sys.stdin.readline().strip()
    comb = sys.stdin.readline().strip()

    total_moves = 0

    for i in range(n):
        initDigit = int(initstate[i])
        targetDig = int(comb[i])
        diff = abs(initDigit - targetDig)
        circular_diff = 10 - diff
        total_moves += min(diff, circular_diff)

    print(total_moves)

solve()