def solve():
    n = int(input())
    h = list(map(int, input().split()))

    s = 0 
    
    for i in range(n):
        s += h[i] 
        if s < i:
            print("NO")
            return
        
        s -= i
            
    print("YES")

t = int(input())
for _ in range(t):
    solve()