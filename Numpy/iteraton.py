import numpy as np

arr = np.array([10, 20, 30, 40])

for x in arr:
    print(x)


# for 2D

arr2d = np.array([[1, 2, 3], [4, 5, 6]])

for row in arr2d:
    print(row)

# To access elements inside each row:

for row in arr2d:
    for elem in row:
        print(elem)


# 3d array iteration

arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

for matrix in arr3d:        # Each "matrix"
    print("Matrix:")
    for row in matrix:      # Each row inside matrix
        for elem in row:    # Each element
            print(elem)

# Efficient Way
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in np.nditer(arr):
    print(x)

# Iterating With Index
arr = np.array([[1, 2, 3], [4, 5, 6]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)
