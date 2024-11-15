#1
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

#2
import numpy as np

def rearrange_matrix(matrix):
    max_value = -float('inf')
    max_position = (-1, -1)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > max_value:
                max_value = matrix[i, j]
                max_position = (i, j)
    max_row, max_col = max_position
    if max_row != 0:
        matrix[[0, max_row]] = matrix[[max_row, 0]]

    if max_col != 0:
        matrix[:, [0, max_col]] = matrix[:, [max_col, 0]]

    return matrix
