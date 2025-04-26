import sys

def solve():
  s = sys.stdin.readline().strip()
  stack = []

  for char in s:
    if char == 'A':
      stack.append(char)
    elif char == 'B':
      if stack and (stack[-1] == 'A' or stack[-1] == 'B'):
        stack.pop()
      else:
        stack.append(char)

  print(len(stack))


t = int(sys.stdin.readline())
for _ in range(t):
  solve()

