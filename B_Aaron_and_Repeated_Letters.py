import sys
def solve(s):
  stack = [] 
  for char in s:
    if stack and stack[-1] == char:
      stack.pop()
    else:
      stack.append(char)

  return "".join(stack)

input_string = sys.stdin.readline().strip()
result_string = solve(input_string)
sys.stdout.write(result_string + "\n")

