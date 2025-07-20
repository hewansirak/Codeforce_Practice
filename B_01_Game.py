import sys
def solve():
    s = sys.stdin.readline().strip() 
    count0 = s.count('0')
    count1 = s.count('1')
    min_chars = min(count0, count1)

    if min_chars % 2 == 1:
        print("DA") 
    else:
        print("NET") 

t = int(sys.stdin.readline())

for _ in range(t):
    solve()

