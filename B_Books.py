def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    max_books = 0
    current_time = 0
    start = 0

    for end in range(n):
        current_time += a[end]

        while current_time > t:
            current_time -= a[start]
            start += 1

        max_books = max(max_books, end - start + 1)

    print(max_books)

solve()