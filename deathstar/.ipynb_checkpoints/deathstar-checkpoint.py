from functools import reduce
n = int(input())
m = []
for _ in range(n):
    m.append([int(i) for i in input().split()])

a = []
for row in m:
    #print(row)
    v=0
    for x in row:
        v |= x
        #print(v, end="-")
    #print("")
    a.append(v)

print(a)
