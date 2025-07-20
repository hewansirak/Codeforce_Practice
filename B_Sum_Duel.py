import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = map(int, input[ptr:ptr+2])
        ptr +=2
        nums = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1
        
        res = 0
        used = defaultdict(int)
        sorted_nums = sorted(freq.keys())
        for num in sorted_nums:
            if used[num] >= freq[num]:
                continue
            complement = k - num
            if complement in freq:
                if complement == num:
                    pairs = freq[num] // 2
                    res += pairs
                    used[num] += pairs * 2
                else:
                    min_pairs = min(freq[num] - used[num], freq[complement] - used[complement])
                    res += min_pairs
                    used[num] += min_pairs
                    used[complement] += min_pairs
        print(res)

solve()