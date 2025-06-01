def solve():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        
        reversed_s = s[::-1]
        
        mirrored_s = []
        for char in reversed_s:
            if char == 'p':
                mirrored_s.append('q')
            elif char == 'q':
                mirrored_s.append('p')
            elif char == 'w':
                mirrored_s.append('w')
        
        results.append("".join(mirrored_s))
    
    for res in results:
        print(res)

solve()