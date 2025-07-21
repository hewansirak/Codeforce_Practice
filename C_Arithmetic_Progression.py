import sys

def solve():
    n = int(sys.stdin.readline())
    if n == 0:
         a_str = sys.stdin.readline() 
         print("0") 
         return
    a = list(map(int, sys.stdin.readline().split()))

    if n == 1:
        print("-1")
        return
    a.sort()
    if a[0] == a[n - 1]:
        print("1")
        print(a[0])
        return

    diffs = []
    for i in range(n - 1):
        diffs.append(a[i + 1] - a[i])

    unique_diffs = sorted(list(set(diffs)))

    if len(unique_diffs) == 1:
        d = unique_diffs[0]
        possible_answers = set()
        possible_answers.add(a[0] - d)
        possible_answers.add(a[n - 1] + d)

        if n == 2 and d > 0 and d % 2 == 0:
             possible_answers.add(a[0] + d // 2) 

        sorted_answers = sorted(list(possible_answers))
        print(len(sorted_answers))
        print(*sorted_answers)
        return
    
    if len(unique_diffs) == 2:
        d1, d2 = unique_diffs[0], unique_diffs[1] 
        if d2 == 2 * d1 and diffs.count(d2) == 1:
            missing_val = -1 
            for i in range(n - 1):
                if a[i + 1] - a[i] == d2:
                    missing_val = a[i] + d1
                    break 

            print("1")
            print(missing_val)
            return
    print("0")

solve()