import numpy as np

def merge_left(matrix):
    new_matrix = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        nums = matrix[i][matrix[i] != 0]
        merged = []
        j = 0
        while j < len(nums):
            if j + 1 < len(nums) and nums[j] == nums[j + 1]:
                merged.append(nums[j] * 2)
                j += 2
            else:
                merged.append(nums[j])
                j += 1
        for j in range(len(merged)):
            new_matrix[i][j] = merged[j]
    return new_matrix

def merge_right(grid):
    return np.fliplr(merge_left(np.fliplr(grid)))

def merge_up(grid):
    return merge_left(grid.T).T

def merge_down(grid):
    return merge_right(grid.T).T

def get_input():
    matrix = np.zeros((5, 5), dtype=int)
    for i in range(4):
        row = input().strip().split()
        for j, val in enumerate(row):
            matrix[i][j] = int(val)
    move = int(input())
    return matrix, move

def process_move(matrix, move):
    if move == 0:
        return merge_left(matrix)
    elif move == 1:
        return merge_up(matrix)
    elif move == 2:
        return merge_right(matrix)
    elif move == 3:
        return merge_down(matrix)

matrix, move = get_input()
result = process_move(matrix, move)
print(result)
