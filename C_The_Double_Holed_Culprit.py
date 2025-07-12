def solve():
    n = int(input())
    p_input = list(map(int, input().split()))
    p_values = [x - 1 for x in p_input] 

    results = []
    for start in range(n):
        visited = [False] * n
        curr = start

        while True:
            visited[curr] = True

            next = p_values[curr]

            if visited[next]:
                results.append(next + 1) 
                break
            else:
                curr = next
    
    print(*(results))

solve()