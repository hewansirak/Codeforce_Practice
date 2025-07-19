def longest_good_segment(n, s, a):
    
    max_length = 0
    left = 0
    current_sum = 0

    for right in range(n):
        current_sum += a[right]

        while current_sum > s:
            current_sum -= a[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    result = longest_good_segment(n, s, a)
    print(result)