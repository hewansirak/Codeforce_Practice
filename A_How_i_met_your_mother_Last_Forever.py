def solve():
    n = int(input())
    s = input()
    count_n = s.count('n')
    count_z = s.count('z')
    result = ['1'] * count_n + ['0'] * count_z

    print(*result)

solve()