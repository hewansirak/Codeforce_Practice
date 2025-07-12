n = int(input())
crew = []
for i in range(n):
    name, status = input().split()
    crew.append((name, status, i))  

def get_priority(status):
    if status == 'rat':
        return 1
    elif status == 'woman' or status == 'child':
        return 2
    elif status == 'man':
        return 3
    elif status == 'captain':
        return 4
    else:
        return 5  

crew_sorted = sorted(crew, key=lambda x: (get_priority(x[1]), x[2]))

for member in crew_sorted:
    print(member[0])