import sys
from collections import deque 

def solve():
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))

    visited = [[False for _ in range(m)] for _ in range(n)]
    max_volume = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(n):
        for c in range(m):
            if grid[r][c] > 0 and not visited[r][c]:
                current_lake_volume = 0
                q = deque([(r, c)])
                visited[r][c] = True

                while q:
                    curr_r, curr_c = q.popleft()
                    current_lake_volume += grid[curr_r][curr_c]

                    for i in range(4):
                        next_r, next_c = curr_r + dr[i], curr_c + dc[i]

                        if 0 <= next_r < n and 0 <= next_c < m:
                            if grid[next_r][next_c] > 0 and not visited[next_r][next_c]:
                                visited[next_r][next_c] = True
                                q.append((next_r, next_c))
                
                max_volume = max(max_volume, current_lake_volume)
    
    sys.stdout.write(str(max_volume) + "\n")

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()