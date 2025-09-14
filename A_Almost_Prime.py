n = int(input())
count = [0] * (n + 1)

for p in range(2, n + 1):
    if count[p] == 0:  # p is prime
        for multiple in range(p, n + 1, p):
            count[multiple] += 1

result = sum(1 for i in range(1, n + 1) if count[i] == 2)
print(result)
