def solve():
    n, m, k = map(int, input().split())
    a = sorted(list(input()))
    b = sorted(list(input()))
    
    c = ""
    a_count = 0
    b_count = 0
    
    a_ptr = 0
    b_ptr = 0
    
    while a_ptr < n and b_ptr < m:
        if a[a_ptr] < b[b_ptr]:
            if a_count < k:
                c += a[a_ptr]
                a_ptr += 1
                a_count += 1
                b_count = 0
            else:
                c += b[b_ptr]
                b_ptr += 1
                b_count += 1
                a_count = 0
        else:
            if b_count < k:
                c += b[b_ptr]
                b_ptr += 1
                b_count += 1
                a_count = 0
            else:
                c += a[a_ptr]
                a_ptr += 1
                a_count += 1
                b_count = 0
                
    print(c)

t = int(input())
for _ in range(t):
    solve()