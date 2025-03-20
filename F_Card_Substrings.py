def solve():
    n, m = map(int, input().split())
    s = input()
    cards = sorted(list(input()))

    def check(substring, cards_available):
        cards_copy = cards_available[:]
        for char in substring:
            if char in cards_copy:
                cards_copy.remove(char)
            else:
                return False
        return True

    count = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if check(substring, cards):
                count += 1
    print(count)

solve()