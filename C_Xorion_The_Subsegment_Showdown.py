def solve():
    x, y = map(int, input().split())
    
    result = x ^ y
    if result == 0:
        print(1)  
    else:
        lsb = result & -result
        print(lsb)


t = int(input())
for _ in range(t):
    solve()
