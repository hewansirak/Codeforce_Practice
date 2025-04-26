import sys
def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        nameparts = sys.stdin.readline().split()
        modern_name = nameparts[0][0] + nameparts[1][0] + nameparts[2][0]
        print(modern_name)

solve()