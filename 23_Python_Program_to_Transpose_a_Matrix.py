def transpose_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)


# import numpy as np

# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

# transposed_matrix = np.transpose(matrix)
# print(transposed_matrix)
