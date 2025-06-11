def solve():
    n, k, q = map(int, input().split())
    max_temp = 200000  
    counts = [0] * (max_temp + 2)  
    
    for _ in range(n):
        l, r = map(int, input().split())
        counts[l] += 1
        counts[r + 1] -= 1
        
    for i in range(1, max_temp + 1):
        counts[i] += counts[i - 1]
    
    for i in range(1, max_temp + 1):
        if counts[i] >= k:
            counts[i] = 1
        else:
            counts[i] = 0
            
    for i in range(1, max_temp + 1):
        counts[i] += counts[i - 1]
        
    for _ in range(q):
        a, b = map(int, input().split())
        result = counts[b] - counts[a - 1]
        print(result)

solve()