import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(np.min(arr))       # 10
print(np.max(arr))       # 90

print(np.min(arr, axis=0))   # Column-wise min -> [10 20 30]
print(np.max(arr, axis=1))   # Row-wise max   -> [30 60 90]

print(np.argmin(arr))   # 0 (index of smallest element: 10)
print(np.argmax(arr))   # 8 (index of largest element: 90)

print(np.mean(arr))     # 50.0
print(np.median(arr))   # 50.0

print(np.std(arr))   # 25.819 (spread of data)
print(np.var(arr))   # 667.0  (variance)

print(np.cumsum(arr))  
# [ 10  30  60 100 150 210 280 360 450]

print(np.cumprod(arr))  
# [       10       200      6000   240000 12000000 720000000
#   50400000000 4032000000000 362880000000000]
