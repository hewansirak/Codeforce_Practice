import sys

def solve():
    n = int(sys.stdin.readline())

    if n == 0:
        h_str = sys.stdin.readline() 
        print(0)
        return

    h = list(map(int, sys.stdin.readline().split()))

    if n == 1:
        print(1)
        return

    prefmax = [0] * n
    current_max = -1 
    for i in range(n):
        current_max = max(current_max, h[i])
        prefmax[i] = current_max
    suffmin = [0] * (n + 1)
    suffmin[n] = float('inf') 
    current_min = float('inf')

    for i in range(n - 1, -1, -1):
        current_min = min(current_min, h[i])
        suffmin[i] = current_min
    block_count = 0

    for i in range(n):
        if prefmax[i] <= suffmin[i + 1]:
            block_count += 1

    print(block_count)

solve()