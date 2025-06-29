t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    found = False
    l, r = -1, -1
    # Iterate over all possible starting indices
    for i in range(n):
        # Iterate over all possible ending indices >= starting index
        for j in range(i, n):
            # Count 'a's and 'b's in the substring s[i..j]
            count_a = s[i:j+1].count('a')
            count_b = s[i:j+1].count('b')
            # Check if the substring is balanced
            if count_a == count_b and (j - i + 1) > 0:
                l, r = i + 1, j + 1  # Convert to 1-based indexing
                found = True
                break
        if found:
            break
    if found:
        print(l, r)
    else:
        print(-1, -1)