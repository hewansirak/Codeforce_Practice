import sys
n = int(sys.stdin.readline())
percentages = list(map(int, sys.stdin.readline().split()))
total_sum = sum(percentages)
cocktail_percentage = total_sum / n
print(f"{cocktail_percentage:.12f}")
