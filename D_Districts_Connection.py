import sys

def solve():
    n_str = sys.stdin.readline()
    if not n_str: return
    n = int(n_str)
    a = list(map(int, sys.stdin.readline().split()))

    if len(set(a)) == 1:
        print("NO")
        return

    print("YES")

    secondary_hub_idx = -1
    for i in range(1, n):
        if a[i] != a[0]:
            secondary_hub_idx = i
            break
    
   