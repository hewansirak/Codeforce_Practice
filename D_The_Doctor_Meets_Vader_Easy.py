import sys
from bisect import bisect_right

s, b = map(int, sys.stdin.readline().split())
spaceship_attack = list(map(int, sys.stdin.readline().split()))

bases = []
for _ in range(b):
    d, g = map(int, sys.stdin.readline().split())
    bases.append((d, g))

bases.sort()

sorted_defenses = [base[0] for base in bases]
sorted_gold = [base[1] for base in bases]

prefix_gold = [0] * b
if b > 0:
    prefix_gold[0] = sorted_gold[0]
    for i in range(1, b):
        prefix_gold[i] = prefix_gold[i-1] + sorted_gold[i]

def get_prefix_sum(index):
    if index < 0:
        return 0
    if index >= len(prefix_gold):
        return prefix_gold[-1] if prefix_gold else 0 
    return prefix_gold[index]

results = []
for attack_power in spaceship_attack:
    count_bases_attackable = bisect_right(sorted_defenses, attack_power)
    total_gold = get_prefix_sum(count_bases_attackable - 1)
    results.append(total_gold)

print(*results)