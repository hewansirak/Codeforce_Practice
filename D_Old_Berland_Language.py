import sys

def solve_d():
    # Set up input reading
    try:
        # Read N
        n_line = sys.stdin.readline()
        if not n_line: return print("NO")
        N = int(n_line.strip())
        
        # Read lengths
        lengths = list(map(int, sys.stdin.readline().split()))
    except:
        return print("NO")

    indexed_lengths = []
    for i in range(N):
        indexed_lengths.append((lengths[i], i))

    indexed_lengths.sort()

    result_words = [""] * N

    available_prefixes = {(1, '0'), (1, '1')} 

    current_idx = 0
    while current_idx < N:
        required_len, original_index = indexed_lengths[current_idx]
        current_idx += 1
        
        best_prefix = None
        best_len = float('inf')
        
        for length, prefix in available_prefixes:
            if length <= required_len:
                if length < best_len:
                    best_len = length
                    best_prefix = prefix
                elif length == best_len and prefix < best_prefix:
                    best_prefix = prefix
        
        if best_prefix is None:
            return print("NO")

        available_prefixes.remove((best_len, best_prefix))

        padding = '0' * (required_len - best_len)
        word = best_prefix + padding
        result_words[original_index] = word

        temp_word = list(word)
        found_flip = False
        
        for k in range(required_len - 1, -1, -1):
            if temp_word[k] == '0':
                temp_word[k] = '1'
                
                new_base_str = "".join(temp_word[:k+1])
                new_base_len = k + 1
                
                available_prefixes.add((new_base_len, new_base_str))
                found_flip = True
                break

    print("YES")
    for word in result_words:
        print(word)

if __name__ == "__main__":
    solve_d()