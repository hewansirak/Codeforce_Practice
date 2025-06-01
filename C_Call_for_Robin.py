import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n <= 2:
        print("-1")
        return

    a.sort()
    init_sum = sum(a)
    num_dis = (n // 2) + 1

    target_dis = a[num_dis - 1]
    x_min_val = max(0, 2 * n * target_dis - init_sum + 1)

    numer = init_sum - 2 * n * a[n-1]
    denom = 2 * n - 1

    x_min = 0
    if numer > 0:
        x_min = (numer + denom - 1) // denom
    else:
        x_min = numer // denom
        if numer % denom != 0:
            x_min += 1

    ans_x = max(x_min_val, x_min)

    print(ans_x)

t = int(input())
for _ in range(t):
    solve()