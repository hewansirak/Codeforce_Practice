def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if all(a[i] <= a[i+1] for i in range(n-1)):
        print("NO")
        return

    print("YES")

t = int(input())
for _ in range(t):
    solve()