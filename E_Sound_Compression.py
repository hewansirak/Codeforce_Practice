n, I = map(int, input().split())
a = list(map(int, input().split()))

max_bits_per_val = (8 * I) // n


allowed_distinct_values = 2 ** max_bits_per_val
a.sort()

unique_vals = []
counts = []

if n > 0:
    unique_vals.append(a[0])
    counts.append(1)
    for i in range(1, n):
        if a[i] == a[i - 1]:
            counts[-1] += 1
        else:
            unique_vals.append(a[i])
            counts.append(1)

k = len(unique_vals)


if k <= allowed_distinct_values:
    print(0)
else:

    prefix_sum_counts = [0] * (k + 1)
    for i in range(k):
        prefix_sum_counts[i + 1] = prefix_sum_counts[i] + counts[i]
    

    max_kept = 0
    window_len = allowed_distinct_values

    for i in range(k - window_len + 1):
        kept_in_window = prefix_sum_counts[i + window_len] - prefix_sum_counts[i]
        if kept_in_window > max_kept:
            max_kept = kept_in_window
    print(n - max_kept)
    