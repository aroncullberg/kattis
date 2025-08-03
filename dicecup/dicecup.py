a, b = sorted(list(map(int, input().split())))

print('\n'.join(str(i+1) for i in range(a, b+1)))
