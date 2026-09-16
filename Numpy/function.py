import numpy as np
var = np.array([1,23,3,4,5,6,9,8,7,2,5,4,6,5])

# x=np.where(var == 5)
x=np.where(var%2 == 0)
print(x)

# numpy.searchsorted()
arr = np.array([10, 20, 30, 40, 50])   # must be sorted
pos = np.searchsorted(arr, 25)
print(pos)

# filter 
