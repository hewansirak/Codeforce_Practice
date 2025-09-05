import math

def solve():

    n = int(input())
    a = list(map(int, input().split()))
    
    curr = 0
    for num in a:
        curr = math.gcd(curr, num)
    
    if curr in a:
        print(curr)
    else:
        print(-1)

solve()