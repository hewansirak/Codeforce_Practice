a, b = map(int, input().split())

sequence = []
current = b
found = False

while current >= a:
    if current == a:
        found = True
        break
    if current % 2 == 0:
        current = current // 2
        sequence.append(current)
    else:
        if str(current)[-1] == '1':
            current = (current - 1) // 10
            sequence.append(current)
        else:
            break

if found:
    print("YES")
    sequence.reverse()
    sequence = [a] + sequence
    print(len(sequence))
    print(' '.join(map(str, sequence)))
else:
    print("NO")