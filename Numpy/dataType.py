import numpy as np

# Integer
a = np.array([1, 2, 3], dtype=np.int32)
print(a, a.dtype)  
# [1 2 3] int32

# Unsigned Integer
b = np.array([1, 2, 255], dtype=np.uint8)
print(b, b.dtype)  
# [  1   2 255] uint8

# Float
c = np.array([3.14, 2.71], dtype=np.float64)
print(c, c.dtype)  
# [3.14 2.71] float64

# Complex
d = np.array([1+2j, 3+4j], dtype=np.complex64)
print(d, d.dtype)  
# [1.+2.j 3.+4.j] complex64

# Boolean
e = np.array([True, False, True], dtype=bool)
print(e, e.dtype)  
# [ True False  True] bool

# String
f = np.array(["hello", "world"], dtype='U5')
print(f, f.dtype)  
# ['hello' 'world'] <U5
