import numpy as np

# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])

# print(arr.shape)


# reshape
arr = np.array([1, 2, 3, 4, 5, 6] , ndmin=4)
# reshaped = arr.reshape(2, 3)

print(arr)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped = arr.reshape(2, 2, 2)  

print(reshaped)
