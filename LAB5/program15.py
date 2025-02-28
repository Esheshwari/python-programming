import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
result = np.matmul(arr1, arr2) # or arr1 @ arr2
print(result)
# Output:
# [[19 22]
# [43 50]]
