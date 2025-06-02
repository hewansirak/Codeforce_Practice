import sys
import math

def solve():

    l, r = map(int, sys.stdin.readline().split())
    diff = r - l
    val_inside_sqrt = 1 + 8 * diff

    sqrt_val = math.sqrt(val_inside_sqrt)
    ans = math.floor((1 + sqrt_val) / 2)
    
    print(int(ans))


t = int(sys.stdin.readline())

for _ in range(t):
    solve()