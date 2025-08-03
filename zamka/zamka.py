low = int(input())
high = int(input())
numsumtarget = int(input())

first = None
last = None

for number in range(low, high+1):
    numsum = sum(list(map(int, list(str(number)))))
    if numsum != numsumtarget:
        continue

    if first == None:
        first = number

    last = number

print(first)
print(last)