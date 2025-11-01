import sys
def solve():
    try:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
    except:
        return 0
    
    MAX_BITS = 60

    trie = {}

    def insert(val):
        """Inserts a number into the trie."""
        node = trie
        for bit in range(MAX_BITS - 1, -1, -1):
            b = (val >> bit) & 1
            if b not in node:
                node[b] = {}
            node = node[b]

    def query_max_xor(val):
        """Finds the maximum XOR between val and any number in the trie."""
        node = trie
        max_xor = 0
        if not node:
            return 0
            
        for bit in range(MAX_BITS - 1, -1, -1):
            b = (val >> bit) & 1
            target_b = 1 - b
            
            if target_b in node:
                max_xor |= (1 << bit)
                node = node[target_b]
            elif b in node:
                node = node[b]
            else:
                return 0
                
        return max_xor

    P = [0] * (n + 1)
    for i in range(n):
        P[i+1] = P[i] ^ a[i]
        
    P_n = P[n] 
    
    max_pleasure = 0
    for k in range(n + 1):
        insert(P[k])
        
        B_k = P[k] ^ P_n
        
        current_max_xor = query_max_xor(B_k)
        
        max_pleasure = max(max_pleasure, current_max_xor)

    print(max_pleasure)

solve()