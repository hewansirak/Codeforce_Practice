import sys

def solve():
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))

    if n < 2:
        print(0)
        return

    lengths = []
    current = 1
    for i in range(1, n):
        if t[i] == t[i-1]:
            current += 1
        else:
            lengths.append(current)
            current = 1
    lengths.append(current)

    max_len = 0
    for i in range(len(lengths) - 1):
        max_len = max(max_len, 2 * min(lengths[i], lengths[i+1]))

    print(max_len)

solve()