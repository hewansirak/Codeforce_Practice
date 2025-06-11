def solve():
    n, m, k = map(int, input().split())
    a, b = sorted(input()), sorted(input())
    
    c = []  
    a_ptr, b_ptr = 0, 0
    a_count, b_count = 0, 0

    while a_ptr < n and b_ptr < m:
        x = (a[a_ptr] < b[b_ptr] and a_count < k) or b_count == k
        
        if x:
            c.append(a[a_ptr])
            a_ptr += 1
            a_count += 1
            b_count = 0  
        else:
            c.append(b[b_ptr])
            b_ptr += 1
            b_count += 1
            a_count = 0 
    
    print("".join(c))  

t = int(input())
for _ in range(t):
    solve()
