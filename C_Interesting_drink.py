import sys
import bisect

input = sys.stdin.readline

def solve():

    n = int(input())
    prices = list(map(int, input().split()))
    prices.sort() 

    q = int(input())
    for _ in range(q): 
        m = int(input())
        count = bisect.bisect_right(prices, m)

        print(count)
solve()