import sys
a, b = map(int, input().split())
dict = {}
for _ in range(a):
    job, pay = input().split()
    dict.update({job: int(pay)})

lines = sys.stdin.read().splitlines()
sumsum = 0
for line in lines:
    if line == ".":
        if sumsum != 0:
            print(sumsum)
        sumsum = 0
        continue
    sumsum += sum(dict.get(w,0) for w in line.split())
# print(dict)