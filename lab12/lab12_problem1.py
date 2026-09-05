import numpy as np

arr = np.array([12, 5, 8, 1, 19, 3])
k = 3

result = np.partition(arr, k-1)[:k]

print(result)