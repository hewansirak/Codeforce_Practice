import sys
from collections import defaultdict

def min_steps(test_cases):
    results = []
    for case in test_cases:
        n, m, grid = case
        color_count = defaultdict(int)
        for row in grid:
            for color in row:
                color_count[color] += 1
        max_count = max(color_count.values())
        if max_count == n * m:
            results.append(0)
            continue
        # The maximum number of cells that can be painted in one step is ceil(max_count / 2)
        # Because in a grid, the maximum independent set is roughly half the total cells
        steps = (max_count + 1) // 2
        results.append(steps)
    return results

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    test_cases = []
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        grid = []
        for _ in range(n):
            row = list(map(int, input[idx:idx + m]))
            grid.append(row)
            idx += m
        test_cases.append((n, m, grid))
    results = min_steps(test_cases)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()