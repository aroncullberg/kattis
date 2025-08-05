n = int(input())

EMAX = 10**5
E = 0

game = set()

largest_quest = (0, 0)


def add(E: int, G: int):
    global largest_quest
    game.add((E, G))
    if E > largest_quest[0]:
        largest_quest = (E, G)


def query(X: int):
    pass


for _ in range(n):
    lst = input().split()

    # print(str)
    op = lst[0]
    if op == "add":
        add(int(lst[1]), int(lst[2]))
    elif op == "query":
        query(int(lst[1]))
