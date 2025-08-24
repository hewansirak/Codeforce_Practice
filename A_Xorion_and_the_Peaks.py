t = int(input().strip())
results = []
for _ in range(t):
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    max_peaks = (n - 1) // 2
    if k > max_peaks:
        results.append("-1")
    else:
        res = []
        low = 1
        high = n
        for i in range(n):
            if i % 2 == 1 and k > 0:
                res.append(high)
                high -= 1
                k -= 1
            else:
                res.append(low)
                low += 1
        results.append(" ".join(map(str, res)))

for res in results:
    print(res)