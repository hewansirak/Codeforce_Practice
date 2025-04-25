import sys

def solve():
    s = sys.stdin.readline().strip() 
    working_keys = set()             
    n = len(s)
    i = 0

    while i < n:
        current_char = s[i]
        j = i 

        while j + 1 < n and s[j + 1] == current_char:
            j += 1

        block_length = (j - i) + 1

        if block_length % 2 != 0:
            working_keys.add(current_char)

        i = j + 1

    sorted_keys = sorted(list(working_keys))
    print("".join(sorted_keys))

q = int(sys.stdin.readline())

for _ in range(q):
    solve()