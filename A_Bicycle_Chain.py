def solve():  
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    max_ratio = 0
    count = 0



    for i in range(n):
        for j in range(m):
            if b[j] % a[i] == 0:
                ratio = b[j] // a[i]
                if ratio > max_ratio:
                    max_ratio = ratio
                    count = 1
                elif ratio == max_ratio:
                    count +=1
    print(count)
solve()