import sys
sys.setrecursionlimit(10**6)

n = int(input())
words = {}
for i in range(n):
    words[i+1] = [input().strip()]

last_active = None
for _ in range(n-1):
    a, b = map(int, input().split())

    words[a] = words[a] + words[b]
    del words[b]

    last_active = a

print(words[last_active])
# print(''.join(words[last_active]))
