import sys

s = sys.stdin.readline().strip()
level = 0
min_level = 0

for char in s:
    if char == '+':
        level += 1
    elif char == '-':
        level -= 1

    min_level = min(min_level, level)

if level == min_level:
    sys.stdout.write("No\n")
else:
    sys.stdout.write("Yes\n")

