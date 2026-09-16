import numpy as np 


# arr_zero =np.zeros(4)
# arr_zero =np.zeros((4,4))
# print(arr_zero)


# 1 array 

# arr_one =np.ones(4)
# print(arr_one)

# empty
# np.empty  gives us empty array


# for identity matrix
print(np.identity(4))  

print(np.eye(4))  


print(np.diag([1, 2, 3])) 

# random number
arr = np.random.rand(2, 3)
print(arr)
# Example Output (changes every time):
# [[0.743 0.682 0.957]
#  [0.123 0.531 0.845]]


arr = np.random.randint(1, 10, (2, 3))
print(arr)
# Example:
# [[7 2 9]
#  [1 6 4]]


arr = np.random.choice([10, 20, 30, 40], size=(2, 2))
print(arr)
# Example:
# [[30 20]
#  [40 10]]
