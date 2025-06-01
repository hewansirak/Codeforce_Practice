import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    for num in a:
        if num < 0:
            print(num)
            return
        
        sqrt_num = int(math.sqrt(num))
        
        if sqrt_num * sqrt_num != num:
            print(num)
            return
solve()