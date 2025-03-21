def matches_template(a, s):
    if len(a) != len(s):
        return False
    
    a_to_s = {}
    s_to_a = {}
    
    for i in range(len(a)):
        if a[i] in a_to_s:
            if a_to_s[a[i]] != s[i]:
                return False
        else:
            a_to_s[a[i]] = s[i]
        
        if s[i] in s_to_a:
            if s_to_a[s[i]] != a[i]:
                return False
        else:
            s_to_a[s[i]] = a[i]
    
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        s = input().strip()
        if matches_template(a, s):
            print("YES")
        else:
            print("NO")