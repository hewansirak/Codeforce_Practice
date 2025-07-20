def max_speed(n, k, speeds):
    speeds.sort(reverse=True)
    return speeds[k - 1]

n, k = map(int, input().split())
speeds = list(map(int, input().split()))

print(max_speed(n, k, speeds))