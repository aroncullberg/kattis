import time

N, t = map(int, input().split())

list = list(map(int, input().split()))

if t == 1:
    print(7)

if t == 2:
    if list[0] > list[1]:
        print("Bigger")
    elif list[0] == list[1]:
        print("Equal")
    else:
        print("Smaller")

if t == 3:
    print(sorted(list[:3])[1])


if t == 4:
    print(sum(list))

if t == 5:
    print(sum([x for x in list if x % 2 == 0]))

if t == 6:
    a = 'abcdefghijklmnopqrstuvwxyz'
    list = [a[x%26] for x in list]
    print(''.join(list))

if t == 7:
    visited = [False] * N
    i = 0
    start = time.time()
    while True:
        if i == N-1:
            print("Done")
            break
        if i < 0 or i >= N:
            print("Out")
            break
        if visited[i]:
            print("Cyclic")
            break
        visited[i] = True
        i = list[i]
