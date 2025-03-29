def solve():
    n = int(input())
    s = input()
    solved = set()
    candies = 0
    for problem in s:
        if problem not in solved:
            candies += 2
            solved.add(problem)
        else:
            candies += 1
    print(candies)

t = int(input())
for _ in range(t):
    solve()