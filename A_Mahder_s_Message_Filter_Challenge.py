def solve():
  n = int(input())
  s = input()
  
  count_right_parentheses = 0
  for i in range(n - 1, -1, -1):
    if s[i] == ')':
      count_right_parentheses += 1
    else:
      break
  
  if count_right_parentheses > n - count_right_parentheses:
    print("Yes")
  else:
    print("No")

t = int(input())
for _ in range(t):
  solve()