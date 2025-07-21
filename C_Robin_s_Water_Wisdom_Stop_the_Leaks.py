n, A, B = map(int, input().split())
s = list(map(int, input().split()))

s1 = s[0]

if s1 == 0:
    if B == 0:
        print(0)
    else:
        print(-1)
    exit()

target_sum = (s1 * A) / B
total_sum = sum(s)

if total_sum <= target_sum:
    print(0)
else:
    other_sizes = sorted(s[1:])
    blocked = 0
    for size in other_sizes:
        total_sum -= size
        blocked += 1
        if total_sum <= target_sum:
            print(blocked)
            break
    else:
        if s1 <= target_sum:
            print(n - 1)
        else:
            print(-1)