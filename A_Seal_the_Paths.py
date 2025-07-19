n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))
 
visited = [[False]*m for _ in range(n)]
indexes = []
 
if k == 0:
    for row in arr:
        print(''.join(row))
    quit()
 
def dfs(x, y):
    stack = [(x,y)]
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        
        visited[x][y] = True
        indexes.append((x, y))
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.' and not visited[nx][ny]:
                stack.append((nx, ny))
 
found = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == '.':
            dfs(i, j)
            found = True
            break
    if found:
        break
 
for x, y in indexes[-k:]:
    arr[x][y] = 'X'
for row in arr:
    print(''.join(row))
            