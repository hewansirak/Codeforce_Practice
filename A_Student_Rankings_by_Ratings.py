n = int(input())
a = list(map(int, input().split()))

r = []
for x in a:
    c = 0
    for y in a:
        if y > x:
            c += 1
    r.append(c + 1)

print(*r)