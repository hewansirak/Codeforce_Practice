import sys
from collections import defaultdict, deque, Counter

input = lambda: sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())

for _ in range(RI()):
    n, m = RII()
    a = RILIST()
    s = input()

    l = 0
    r = n - 1
    b = []

    for c in s:
        if c == 'L':
            b.append(a[l])
            l += 1
        elif c == 'R':
            b.append(a[r])
            r -= 1

    vas = 1
    c = []
    for i in range(n):
        vas = vas * b[n - 1 - i] % m
        c.append(vas)

    print(*reversed(c))