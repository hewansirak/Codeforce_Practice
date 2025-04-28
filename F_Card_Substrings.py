from collections import Counter
def solve():
    n, m = map(int, input().split())
    s = input()
    cards = input()
    
    cards_count = Counter(cards)
    s_count = Counter()
    left = 0
    ans = 0

    for right in range(n):
        s_count[s[right]] += 1
        while s_count[s[right]] > cards_count[s[right]]:
            s_count[s[left]] -= 1
            left += 1
        ans += (right - left + 1)
    
    print(ans)

solve()