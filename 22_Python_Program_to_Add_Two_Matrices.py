def add_matrices(X, Y):
    result = []
    for i in range(len(X)):
        row = []
        for j in range(len(X[0])):
            row.append(X[i][j] + Y[i][j])
        result.append(row)
    return result

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = add_matrices(X, Y)
for row in result:
    print(row)


# import numpy as np

# X = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# Y = np.array([[9, 8, 7],
#               [6, 5, 4],
#               [3, 2, 1]])

# result = X + Y
# print(result)
