import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = input[ptr]
        ptr += 1
        b = input[ptr]
        ptr += 1
        
        if all(c == '0' for c in a):
            results.append("YES")
            continue
        
        possible = True
        carry = 0
        for i in range(n-1, 0, -1):
            current_a = a[i]
            current_b = b[i-1]
            effective_a = current_a
            if carry % 2 == 1:
                effective_a = '1' if effective_a == '0' else '0'
            if effective_a == '1':
                if current_b == '0':
                    carry = 0
                else:
                    carry = 1
            else:
                carry = 0
        effective_first_a = a[0]
        if carry % 2 == 1:
            effective_first_a = '1' if effective_first_a == '0' else '0'
        if effective_first_a == '1':
            possible = False
        results.append("YES" if possible else "NO")
    print('\n'.join(results))

solve()