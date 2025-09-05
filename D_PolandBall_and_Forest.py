def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    
    parent = [i for i in range(n + 1)]  
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if u_root < v_root:
            parent[v_root] = u_root
        else:
            parent[u_root] = v_root
    
    for i in range(1, n + 1):
        union(i, p[i - 1])
    
    unique_roots = set()
    for i in range(1, n + 1):
        unique_roots.add(find(i))
    
    print(len(unique_roots))

if __name__ == "__main__":
    main()