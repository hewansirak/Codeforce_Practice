import math
import sys

input = sys.stdin.readline

def solve():

    n = int(input())
    total_squares = sum(map(int, input().split()))
    sqrt_total = math.sqrt(total_squares)
    root_rounded = round(sqrt_total)

    if root_rounded * root_rounded == total_squares:
        print("YES")
    else:
        print("NO")

t = int(input())

for _ in range(t):
    solve()