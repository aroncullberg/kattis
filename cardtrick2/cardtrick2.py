n = int(input())

state = 0
for _ in range(n):
    T = int(input())
    lst = []
    for num in range(T, 0, -1):
        lst.insert(0, num)
        for i in range(num):
            lst.insert(0, lst.pop())
    print(' '.join(map(str, lst)))
