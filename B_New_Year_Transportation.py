import sys

def solve():
    n, t = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    curr = 1 

    while curr < t:
        jump = a[curr - 1]
        curr += jump
    
    if curr == t:
        print("YES")
    else: 
        print("NO")

solve()