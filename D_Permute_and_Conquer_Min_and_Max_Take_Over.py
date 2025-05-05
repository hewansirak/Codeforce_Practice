import sys
from collections import defaultdict, deque, Counter

input = lambda: sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())

for _ in range(RI()):
    n = RI()
    a = RILIST()
    m = [0] * (n + 1)
    for i in range(n):
        m[a[i]] = i
    l = (n + 1) // 2
    r = (n + 2) // 2
    while l > 0 and ((l == r) or ((m[l] < m[l + 1]) and (m[r - 1] < m[r]))):
        l -= 1
        r += 1
    print(l)