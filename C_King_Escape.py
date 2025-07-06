import sys

def solve():
    n = int(sys.stdin.readline())
    ax, ay = map(int, sys.stdin.readline().split())
    bx, by = map(int, sys.stdin.readline().split())
    cx, cy = map(int, sys.stdin.readline().split())

    same_hori = (bx > ax) == (cx > ax)

    same_verii = (by > ay) == (cy > ay)

    if same_hori and same_verii:
        print("YES")
    else:
        print("NO")

solve()

