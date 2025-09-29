n = int(input())

denomi = [100, 20, 10, 5, 1]
total_bills = 0

for d in denomi:
    count = n // d
    
    total_bills += count
    
    n %= d
    
    if n == 0:
        break

print(total_bills)