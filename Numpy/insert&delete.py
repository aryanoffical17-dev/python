# numpy.insert()
import numpy as np

arr = np.array([1, 2, 3, 4])
new_arr = np.insert(arr, 2, 99)
print(new_arr)   # [ 1  2 99  3  4]


# 2D array
arr2d = np.array([[1,2],[3,4]])

# Insert a column (axis=1)
new_arr = np.insert(arr2d, 1, [9,9], axis=1)
print(new_arr)
# [[1 9 2]
#  [3 9 4]]

# Insert a row (axis=0)
new_arr2 = np.insert(arr2d, 1, [7,7], axis=0)
print(new_arr2)
# [[1 2]
#  [7 7]
#  [3 4]]

# numpy.delete()
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.delete(arr, 2)
print(new_arr)   # [10 20 40 50]

arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

# Delete row 1 (axis=0)
print(np.delete(arr2d, 1, axis=0))
# [[1 2 3]
#  [7 8 9]]

# Delete column 2 (axis=1)
print(np.delete(arr2d, 2, axis=1))
# [[1 2]
#  [4 5]
#  [7 8]]
