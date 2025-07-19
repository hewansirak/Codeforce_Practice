def solve():
    n, k1, k2 = map(int, input().split())
    player1_cards = list(map(int, input().split()))
    player2_cards = list(map(int, input().split()))

    if n in player1_cards:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()