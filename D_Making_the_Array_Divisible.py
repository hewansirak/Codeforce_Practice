def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    remainder = {}

    for x in a:
        if x % k != 0:
            rem = k - (x % k)
            if rem not in remainder:
                remainder[rem]= 0
            remainder[rem] +=1

        if not remainder:
            print(0)
            return
        

        max_rem = 0
        max_count = 0

        for rem, count in remainder.items():
            if count > max_count or (count == max_count and rem > max_rem):
                max_count = count
                max_rem = rem

    print((max_count - 1) * k + max_rem + 1)


t = int(input())
for _ in range(t):
    solve()