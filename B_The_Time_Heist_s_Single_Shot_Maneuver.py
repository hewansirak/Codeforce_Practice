def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    def check_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True
    
    if check_sorted(a):
        print("YES")
        return
    
    for i in range(n):
        temp_a = a[:]
        temp_a[i] = b[0] - temp_a[i]
        if check_sorted(temp_a):
            print("YES")
            return

    all_transformed = [b[0] - x for x in a]
    if check_sorted(all_transformed):
        print("YES")
        return
    
    print("NO")
    
t = int(input())
for _ in range(t):
    solve()