import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()

    mex_candidate = 1

    for x in a:
        if x >= mex_candidate:
            mex_candidate += 1

    print(mex_candidate)

solve()