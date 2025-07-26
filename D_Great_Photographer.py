# Among other things, Bob is keen on photography. Especially he likes to take pictures of sportsmen. 
# That was the reason why he placed himself in position x0 of a long straight racetrack and got ready to take pictures. 
# But the problem was that not all the runners passed him. The total amount of sportsmen, training at that racetrack, 
# equals n. And each of them regularly runs distances within a particular segment of the racetrack, 
# which is the same for each sportsman. For example, the first sportsman runs from position a1 to position b1, 
# the second — from a2 to b2

# What is the minimum distance that Bob should move to have a chance to take pictures of each sportsman? 
# Bob can take a picture of a sportsman, if he stands within the segment that this sportsman covers on the racetrack.

n, x0 = map(int, input().split())

L, R = 0, 1000  

for _ in range(n):
    a, b = map(int, input().split())
    L = max(L, min(a, b))  
    R = min(R, max(a, b)) 

if L > R:
    print(-1)
else:
    print(0 if L <= x0 <= R else min(abs(x0 - L), abs(x0 - R)))
