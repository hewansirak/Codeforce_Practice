# Mozart composes melodies. He represents them as a sequence of notes, 
# where each note is encoded as an integer from 0 to 127 inclusive. 
# The interval between two notes a and b is equal to |a−b| semitones.

# Mozart considers a melody perfect if the interval between each two adjacent notes 
# is either 5 semitones or 7 semitones.

# After composing his latest melodies, he enthusiastically shows you his collection of works. 
# Help Boris Notkin understand whether his melodies are perfect.


melody = int(input())  

for _ in range(melody):
    input() 
    melody = list(map(int, input().split()))

    if all(abs(melody[i] - melody[i + 1]) in (5, 7) for i in range(len(melody) - 1)):
        print("YES")
    else:
        print("NO")