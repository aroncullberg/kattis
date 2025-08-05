while True:
    try:
        data = input().strip()
        print(f'{eval(data):.2f}')
    except EOFError:
        break
