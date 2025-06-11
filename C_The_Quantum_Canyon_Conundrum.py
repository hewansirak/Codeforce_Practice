def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    candidates = []
    
    for i in range(n):
        l = i
        while i + 1 < n and a[i] == a[i + 1]:
            i += 1
        r = i
        
        left = (l == 0 or a[l - 1] > a[l])
        right = (r == n - 1 or a[r] < a[r + 1])
        
        if left and right:
            candidates.append((l, r))
    
    if len(candidates) == 1:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()