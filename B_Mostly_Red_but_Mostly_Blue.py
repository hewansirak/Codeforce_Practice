def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    prefix_sums = [0]
    for x in a:
        prefix_sums.append(prefix_sums[-1] + x)

    suffix_sums = [0]
    for x in reversed(a):
        suffix_sums.append(suffix_sums[-1] + x)

    answer = False
    for k in range(1, n + 1):
        if 2 * k + 1 <= n:
            blue_sum = prefix_sums[k + 1]
            red_sum = suffix_sums[k]
            if blue_sum < red_sum:
                answer = True
                break

    if answer:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()