import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    if k == n:
        print(0)
        return

    diff = []
    for i in range(n - 1):
        diff.append(a[i+1] - a[i])

    diff.sort(reverse=True)
    total = a[n-1] - a[0]
    for i in range(k - 1):
        total -= diff[i]

    print(total)

if __name__ == '__main__':
    solve()