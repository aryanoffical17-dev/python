import numpy as np 


# x = np.array([1,2,3,4])
# print(x)
# print(x.ndim)

y = np.array([[1,4,5,6],[4,1,5,4]]) 
print(y)
print(y.ndim)

arn = np.array([1,4,5,4],ndmin=10)
print(arn)
print(arn.ndim)