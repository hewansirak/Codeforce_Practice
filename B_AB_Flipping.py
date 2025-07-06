import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    aidx = -1
    for i in range(n):
        if s[i] == 'A':
            aidx = i
            break
    bidx = -1
    for i in range(n - 1, -1, -1):
        if s[i] == 'B':
            bidx = i
            break

    if aidx == -1 or bidx == -1:
        print(0)
        return
    if aidx > bidx:
        print(0)
        return
    
    print(bidx - aidx)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
    