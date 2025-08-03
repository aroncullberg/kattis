while True:
    n = int(input())
    if n == 0:
        break
    
    menu = {}
    for _ in range(n):
        items = input().split()
        
        name = items[:1][0]
        items = items[1:]

        for item in items:
            if item not in menu.keys():
                menu[item] = set()
            menu[item].add(name)
        
    for key in sorted(menu.keys()):
        print(key, ' '.join(menu[key]))
    print("")