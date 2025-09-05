n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a)

if n == 1:
    print(-1)
else:
    diff_dict = {}
    diffs = []
    for i in range(1, n):
        diffs.append(a_sorted[i] - a_sorted[i-1])
    
    unique_diffs = list(set(diffs))
    unique_diffs.sort()
    
    if len(unique_diffs) == 1:
        d = unique_diffs[0]
        if d == 0:
            print(1)
            print(a_sorted[0])
        else:
            if n == 2:
                if d % 2 == 0:
                    mid = a_sorted[0] + d // 2
                    res = [a_sorted[0] - d, mid, a_sorted[-1] + d]
                    res = list(set(res))
                    res.sort()
                    print(len(res))
                    print(' '.join(map(str, res)))
                else:
                    res = [a_sorted[0] - d, a_sorted[-1] + d]
                    res = list(set(res))
                    res.sort()
                    print(len(res))
                    print(' '.join(map(str, res)))
            else:
                res = [a_sorted[0] - d, a_sorted[-1] + d]
                res = list(set(res))
                res.sort()
                print(len(res))
                print(' '.join(map(str, res)))
    elif len(unique_diffs) > 2:
        print(0)
    else:
        d = min(unique_diffs)
        count_big_diff = 0
        pos = -1
        for i in range(1, n):
            if a_sorted[i] - a_sorted[i-1] != d:
                count_big_diff += 1
                pos = i
        if count_big_diff == 1 and (a_sorted[pos] - a_sorted[pos-1]) == 2 * d:
            candidate = a_sorted[pos-1] + d
            # Check if inserting candidate makes the entire sequence AP with d
            temp = a_sorted.copy()
            temp.insert(pos, candidate)
            new_diffs = []
            for i in range(1, len(temp)):
                new_diffs.append(temp[i] - temp[i-1])
            if len(set(new_diffs)) == 1:
                print(1)
                print(candidate)
            else:
                print(0)
        else:
            print(0)