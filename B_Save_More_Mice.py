import math
import sys

input = sys.stdin.readline

def solve():

    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort(reverse=True)

    saved_count = 0
    cat_pos = 0  

    for mouse_pos in x:
        distance_to_hole = n - mouse_pos

        if mouse_pos > cat_pos:
            cat_pos += distance_to_hole
            saved_count += 1
        else:
            break

    print(saved_count)


t = int(input())

for _ in range(t):
    solve()