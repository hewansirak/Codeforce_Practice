import sys
def solve():
    n, k = map(int, sys.stdin.readline().split())
    
    if k % 2 == 0:
        if n % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")

t = int(sys.stdin.readline())
for _ in range(t):
    solve()