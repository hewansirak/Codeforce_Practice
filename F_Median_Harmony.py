def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    bad_total = 0


    for x in s:
        pre = [0] * (n + 1)
        b = [0] * n
        for i in range(n):
            b[i] = -1 if a[i] > x else 1
            pre[i + 1] = pre[i] + b[i]


        count = dict()
        _sum = 0
        j = 0
        check = False


        for i in range(n):
            if a[i] == x:
                if not check:
                    count[0] = 1
                check = True
                while j < i:
                    count[pre[j + 1]] = count.get(pre[j + 1], 0) + 1
                    j += 1
            _sum += count.get(pre[i + 1], 0)
        bad_total += _sum


    total = n * (n + 1) // 2
    print(total - bad_total)


t = int(input())
for _ in range(t):
    solve()