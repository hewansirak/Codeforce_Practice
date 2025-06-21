import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()

    if n == 0:
        print(0)
        return
    
    max_len = 1
    curr_len = 1

    for i in range(1, n):
        if a[i] - a[i - 1] <= k:
            curr_len += 1
        else:
            curr_len = 1
        
        max_len = max(max_len, curr_len)

    print(n - max_len)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
