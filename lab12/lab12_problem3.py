import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Column sum:", np.sum(arr, axis=0))
print("Row sum:", np.sum(arr, axis=1))