import sys

N, M = 0, 0       
CATS = []  
ADJ = [] 
ANS = 0 

def solve():
    global N, M, CATS, ADJ, ANS 
    N, M = map(int, sys.stdin.readline().split())
    CATS = [0] + list(map(int, sys.stdin.readline().split()))
    ADJ = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().split())
        ADJ[u].append(v)
        ADJ[v].append(u)
    ANS = 0
    stack = [(1, 0, 0)] 

    while stack:
        u, p, current_consecutive_cats = stack.pop()

        if CATS[u] == 1:
            current_consecutive_cats += 1
        else:
            current_consecutive_cats = 0

        if current_consecutive_cats > M:
            continue 

        is_leaf = True
        for v in ADJ[u]:
            if v != p:
                is_leaf = False
                stack.append((v, u, current_consecutive_cats))
        if is_leaf:
            ANS += 1 
    print(ANS)
solve()
