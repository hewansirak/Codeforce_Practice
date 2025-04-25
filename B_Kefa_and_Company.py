import sys

def solve():
    input_lines = sys.stdin.readlines()
    n, d = map(int, input_lines[0].split())

    friends = []
    for i in range(1, n + 1):
        m, s = map(int, input_lines[i].split())
        friends.append((m, s))

    friends.sort()

    max_total_friendship = 0
    current_total_friendship = 0
    left = 0

    for right in range(n):
        current_total_friendship += friends[right][1]

        while friends[right][0] - friends[left][0] >= d:
            current_total_friendship -= friends[left][1]
            left += 1

        max_total_friendship = max(max_total_friendship, current_total_friendship)

    print(max_total_friendship)

solve()