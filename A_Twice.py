def solve():
    n = int(input())
    a = list(map(int, input().split()))

    frequency_map = {}
    for x in a:
        frequency_map[x] = frequency_map.get(x, 0) + 1

    score = 0
    for count in frequency_map.values():
        score += count // 2 

    print(score)

t = int(input())
for _ in range(t):
    solve()