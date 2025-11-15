import sys
import math

input = sys.stdin.readline

def solve():
    
    n = int(input())
    total_square = sum(map(int, input().split())) # 8 16
    square_sqrt = math.sqrt(total_square) # 2.6 4
    sqrt_round = round(square_sqrt) # 2 4
    
    if sqrt_round * sqrt_round == total_square:
        print("YES")
    else:
        print("NO")    
        
t = int(input())




for _ in range (t):
    solve()
    