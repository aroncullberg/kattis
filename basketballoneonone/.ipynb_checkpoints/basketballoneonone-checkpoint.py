import sys

string = sys.stdin.read()

A = 0
B = 0
e = False

for _ in range(int(len(string)/2)):
    (person, point), string = string[:2], string[2:]
    if person == 'A':
        A += int(point)
    if person == 'B':
        B += int(point)
    if A == B == 10:
        e = True
    if e:
        if A >= B + 2:
            print("A")
            break
        if B >= A + 2:
            print("B")
            break
    else: 
        if A >= 11:
            print("A")
            break
        if B >= 11:
            print("B")
            break
