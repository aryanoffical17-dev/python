import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])   # First element
print(arr[-1])  # Last element
print(arr[2])   # Third element


arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[0, 0])   # 10 (row 0, col 0)
print(arr[1, 2])   # 60 (row 1, col 2)
print(arr[2, -1])  # 90 (last row, last column)


arr = np.array([ [[1,2], [3,4]],
                 [[5,6], [7,8]] ])

print(arr[0, 1, 1])  # Block 0, row 1, col 1 → 4
print(arr[1, 0, 0])  # Block 1, row 0, col 0 → 5



# Slicing in Numpy
arr2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
])

print(arr2d[0:2, 1:3])  # [[2 3] [6 7]] → slice rows 0-1, cols 1-2
print(arr2d[:, 2])      # [ 3  7 11] → all rows, only column 2
print(arr2d[1, :])      # [5 6 7 8] → row 1, all columns
print(arr2d[::2, ::2])  # [[1 3] [9 11]] → every 2nd row & col
