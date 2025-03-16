def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if k == 0:
        if n == 0:
            print(1)
            return
        if a[0] == 1:
            print("-1")
        else:
            print(a[0] - 1)
        return

    if k > 0 and k <= n:
        if k == n:
            print(a[n - 1])
            return

        if a[k - 1] == a[k]:
            print("-1")
        else:
            print(a[k - 1])
        return

solve()