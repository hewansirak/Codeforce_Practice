n = int(input())
rating = list(map(int, input().split()))

rank = []

for i in rating:
    count = 0
    for j in rating:
        if j > i:
            count += 1
    rank.append(count + 1)
    
print(*rank)

