s = input()
n = len(s)

strict_alternating = True
for i in range(n - 1):
    if s[i] == s[i + 1]: 
        strict_alternating = False
        break

if strict_alternating:
    print("No")
else:
    print("Yes")
