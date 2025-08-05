import sys
sys.setrecursionlimit(1000000)  # Increase this to a large number

'''
1 <= r, c <= 1000
r: number of rows i.e its the x coordinate
c : number of columns, i.e its the y coordinate

NOTE: remember 0,0 is top left corner

and binary is 0 and decimal is 1
'''
r: int
c: int
n: int
(r, c) = map(int, input().split())

matrix = [[0 for i in range(c)] for j in range(r)]

# is i x or y?
# it is x
for x in range(r):
    matrix[x] = list(input())
# #print(matrix)

n = int(input())
# #print("n: ", n)

'''
1<= r1, r2 <= r
1<= c1, c2 <= c
'''
r1: int
c1: int
r2: int
c2: int


def right(path, r, c) -> bool:
    '''
    returns true of the right cell is the same as the current cell
    and its not trying to move into the path
    '''
    return (True if
            matrix[r][c] == matrix[r][c+1] and not
            (r, c+1) in path else False)


def down(path: [(int, int)], r, c) -> bool:
    '''
    returns true of the down cell is the same as the current cell
    '''
    return (True if
            matrix[r][c] == matrix[r+1][c] and not
            (r+1, c) in path else False)


def left(path: [(int, int)], r, c) -> bool:
    '''
    returns true of the left cell is the same as the current cell
    '''
    return (True if
            matrix[r][c] == matrix[r][c-1] and not
            (r, c-1) in path and c-1 >= 0 else False)


def up(path: [(int, int)], r, c) -> bool:
    '''
    returns true of the up cell is the same as the current cell
    '''
    return (True if matrix[r][c] == matrix[r-1][c] and not
            (r-1, c) in path and
            r - 1 >= 0 else False)


def traverse(path: [], r1: int, c1: int, r2: int, c2: int) -> bool:
    if r1 == r2 and c1 == c2:
        return True

    path.append((r1, c1))

    # try:
    if c1 + 1 < c and right(path, r1, c1):
        if traverse(path, r1, c1+1, r2, c2):
            return True
    # except Exception as e:
    #     pass

    # try:
    if r1 + 1 < r and down(path, r1, c1):
        if traverse(path, r1+1, c1, r2, c2):
            return True
    # except:
    #     return False

    # try:
    if c1 - 1 >= 0 and left(path, r1, c1):
        if traverse(path, r1, c1-1, r2, c2):
            return True
    # except Exception as e:
    #     pass
    #
    # try:
    if r1 - 1 >= 0 and up(path, r1, c1):
        if traverse(path, r1-1, c1, r2, c2):
            return True
    # except Exception as e:
    #     pass

    return False


'''
'binary' if a binary user can move from (r₁, c₁) -> (r₂, c₂)
'decimal' if a decimal user can move from (r₁, c₁) -> (r₂, c₂)
'neither' if none of them are possible
'''
for _ in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    # print(f'traverse value: {traverse([], r1, c1, r2, c2)}')
    if traverse([], r1, c1, r2, c2):
        if matrix[r1][c1] == '1':
            print("decimal")
        elif matrix[r1][c1] == '0':
            print("binary")
    else:
        print("neither")
