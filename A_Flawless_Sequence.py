import sys
import math

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    res = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        
        total_sum = n * (n + 1) // 2
        root = math.isqrt(total_sum)
        if root * root == total_sum:
            res.append(-1)
            continue
             
        perm = []
        used = [False] * (n + 2)
        current_sum = 0
        possible = True

        if n == 1:
            res.append(-1)
        elif n == 4:
            res.append("2 4 1 3")
        elif n == 5:
            res.append("5 1 4 3 2")
        else:
            perm = list(range(n, 0, -1))
            total = 0
            ok = True
            for num in perm:
                total += num
                if math.isqrt(total) ** 2 == total:
                    ok = False
                    break
            if ok:
                res.append(' '.join(map(str, perm)))
            else:
                perm = list(range(1, n+1))
                total = 0
                ok = True
                for num in perm:
                    total += num
                    if math.isqrt(total) ** 2 == total:
                        ok = False
                        break
                if ok:
                    res.append(' '.join(map(str, perm)))
                else:
                    perm = []
                    remaining = list(range(1, n+1))
                    current_sum = 0
                    possible = True
                    for i in range(n):
                        found = False
                        for j in range(len(remaining)-1, -1, -1):
                            num = remaining[j]
                            new_sum = current_sum + num
                            root = math.isqrt(new_sum)
                            if root * root != new_sum:
                                perm.append(num)
                                current_sum = new_sum
                                del remaining[j]
                                found = True
                                break
                        if not found:
                            possible = False
                            break
                    if possible:
                        res.append(' '.join(map(str, perm)))
                    else:
                        res.append(-1)
    print('\n'.join(map(str, res)))

solve()