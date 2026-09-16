# Copy
import numpy as np

arr = np.array([1, 2, 3, 4])
copy_arr = arr.copy()   # makes a new independent array

copy_arr[0] = 99

print("Original:", arr)   # [1 2 3 4]
print("Copy:   ", copy_arr)  # [99  2  3  4]

# View
arr = np.array([1, 2, 3, 4])
view_arr = arr.view()   # creates a view of the same data

view_arr[0] = 99

print("Original:", arr)   # [99  2  3  4]
print("View:   ", view_arr)  # [99  2  3  4]

# joining

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))

# For 2D:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print(np.concatenate((a, b), axis=0))  # join rows

# stack
a = np.array([1, 2])
b = np.array([3, 4])

print(np.stack((a, b), axis=0))  # stack as rows
print(np.stack((a, b), axis=1))  # stack as columns


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack((a, b)))  # [1 2 3 4 5 6]

a2 = np.array([[1], [2], [3]])
b2 = np.array([[4], [5], [6]])

print(np.vstack((a2, b2)))

# Splitting NumPy Arrays

    # np.array_split()
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(np.array_split(arr, 3))

    # np.split()
arr = np.array([1, 2, 3, 4, 5, 6])

print(np.split(arr, 3))

    # np.hsplit() and np.vsplit()
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

print(np.hsplit(arr2d, 2))  # split into 2 column groups
print(np.vsplit(arr2d, 2))  # split into 2 row groups
