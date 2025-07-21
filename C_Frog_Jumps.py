import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)

    max_d = 0
    last_pos = 0 
    for i in range(n):
        if s[i] == 'R':
            current_cell = i + 1
            max_d = max(max_d, current_cell - last_pos)
            last_pos = current_cell
    
    max_d = max(max_d, (n + 1) - last_pos)
    
    sys.stdout.write(str(max_d) + '\n')

t = int(sys.stdin.readline())
for _ in range(t):
    solve()