# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

number = int(input("Enter the size of the pattern:"))

track_num = number

while track_num != 0:
    for i in range(1, number+1):
        print("*", end="")
    track_num = track_num -1
