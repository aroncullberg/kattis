import sys

lines = sys.stdin.read().splitlines()[1:]

for line in lines:
    a,b,c = map(int, line.split())
    # print(a,b,c, end=" ")
    if a + b == c:
        print("Possible")
        continue
    if a - b == c or b - a == c:
        print("Possible")
        continue
    if a * b == c:
        print("Possible")
        continue
    if a / b == c:
        print("Possible")
        continue
    if b / a == c:
        print("Possible")
        continue

    print("Impossible")
