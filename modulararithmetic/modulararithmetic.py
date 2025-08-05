while True:
    n, t = map(int, input().split())
    if n == 0 and t == 0:
        break

    for _ in range(t):
        a, op, b = input().split()

        if op == '/':
            a, b = map(int, [a, b])
            try:
                result = pow(b, -1, n)
                final = (a * result) % n
                print(final)
            except ValueError:
                print(-1)
        else:
            print(eval(a + op + b) % n)
