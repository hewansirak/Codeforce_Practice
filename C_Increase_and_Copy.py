import sys
import math
def solve():
    n = int(sys.stdin.readline())

    if n == 1:
        print(0)
        return

    min_moves = float('inf')
    upper_bound_x = int(math.sqrt(n)) + 5

    for x in range(1, upper_bound_x):
        k = (n + x - 1) // x
        current_moves = (x - 1) + (k - 1)
        min_moves = min(min_moves, current_moves)
    print(min_moves)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()

