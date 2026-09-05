import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([10, 25, 30, 50])

positions = np.where(a == b)

print(positions)