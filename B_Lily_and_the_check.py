import sys

def min_operations(x, y):
    operations = 0
    while y > 0:
        max_jump = x
        while max_jump * 10 <= y:
            max_jump *= 10
        
        operations += y // max_jump
        y %= max_jump
    
    return operations

# Fast input handling (line-by-line processing to avoid SIGTERM)
t = int(sys.stdin.readline().strip())

results = []
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    results.append(str(min_operations(x, y)))

# Fast output to avoid slow I/O
sys.stdout.write("\n".join(results) + "\n")
