import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(a + b)
# [11 22 33 44]

print(a - b)
# [ 9 18 27 36]

print(a * b)
# [10 40 90 160]

print(a / b)
# [10. 10. 10. 10.]

print(a // b)
# [10 10 10 10]

print(a % b)
# [0 0 0 0]

print(a ** 2)
# [100 400 900 1600]

print(a ** b)
# [10^1, 20^2, 30^3, 40^4]
# [1.000e+01 4.000e+02 2.700e+04 2.560e+06]
