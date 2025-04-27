def bounty_dilema(s):
    rel = '='
    for c in s:
        if c == '<' and rel == '>': return '?'
        if c == '>' and rel == '<': return '?'
        if c == '<': rel = '<'
        if c == '>': rel = '>'
    return rel

t = int(input())
for _ in range(t):
    s = input().strip()
    print(bounty_dilema(s))