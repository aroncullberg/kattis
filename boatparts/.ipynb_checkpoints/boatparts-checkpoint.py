import sys
parts, days = map(int, input().split())

pl = set()
for i in range(days):
    pl.add(input())
    print(pl)
    if (len(pl) == parts):
        print(i+1)
        sys.exit()

print("paradox avoided")