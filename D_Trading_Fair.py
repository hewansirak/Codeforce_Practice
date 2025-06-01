import bisect

def solve():
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    arr_a.sort()

    res = []
    for val_b in arr_b:
        count = bisect.bisect_right(arr_a, val_b)
        res.append(count)
    
    print(*res)

solve()