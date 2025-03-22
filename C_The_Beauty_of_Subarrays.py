def solve():
    n = int(input())
    p = list(map(int, input().split()))
    result = ['0'] * n  # Initialize result as a list of '0's

    positions = [0] * (n + 1)
    for i, val in enumerate(p):
        positions[val] = i

    left, right = n, -1
    for m in range(1, n + 1):
        left = min(left, positions[m])
        right = max(right, positions[m])
        if right - left + 1 == m:
            result[m - 1] = '1'

    print(''.join(result))  # Join the list into a string

t = int(input())
for _ in range(t):
    solve()