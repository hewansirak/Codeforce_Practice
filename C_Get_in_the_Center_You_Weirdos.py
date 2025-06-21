def solve():
    n = int(input())
    
    if n == 1:
        print(0)
    else:
        m = (n - 1) // 2

        total = (4 * m * (m + 1) * (2 * m + 1)) // 3
        print(total) 

t = int(input())
for _ in range(t):
    solve()