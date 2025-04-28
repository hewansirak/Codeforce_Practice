import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)

    min_char_s = [''] * n
    min_char_s[n - 1] = s[n - 1]
    for i in range(n - 2, -1, -1):
        min_char_s[i] = min(s[i], min_char_s[i + 1])

    t_stack = []
    u = []
    s_ptr = 0

    while s_ptr < n or t_stack:
        if t_stack and (s_ptr == n or t_stack[-1] <= min_char_s[s_ptr]):
             u.append(t_stack.pop())
        elif s_ptr < n:
            t_stack.append(s[s_ptr])
            s_ptr += 1
        elif t_stack:
             u.append(t_stack.pop())


    print("".join(u))

solve()