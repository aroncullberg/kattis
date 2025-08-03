import sys
n, things = sys.stdin.read().splitlines()
#print(n)
#print(things.split())
things = things.split()
for i in range(1, int(n) + 1):
    #print("HELO", i, things[i-1], things[i-1] == "munble")
    if things[i-1] == "mumble":
        continue
    if things[i-1] != str(i):
        print("something is fishy")
        sys.exit()

print("makes sense")