n = int(input())

opinion_strings = input().split() 

cur_max = 0
for opinion_str in opinion_strings:
    cur_ans = int(opinion_str) 
    cur_max = max(cur_max, cur_ans)

print("HARD" if cur_max > 0 else "EASY")