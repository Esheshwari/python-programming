import numpy as np
arr = np.array([5, 2, 8, 1, 3])
arr2D = np.array([[3, 2, 1], [6, 5, 4]])
# Sorting in ascending order (default)
sorted_arr = np.sort(arr)
print(sorted_arr) # Output: [1 2 3 5 8]
# Sorting in descending order
sorted_desc = np.sort(arr)[::-1]
print(sorted_desc) # Output: [8 5 3 2 1]
# Sort each row
sorted_rows = np.sort(arr2D, axis=0) # [[3 2 1]
print(sorted_rows) # [6 5 4]]
# Sort each row # Output:
sorted_cols = np.sort(arr2D, axis=1) # [[1 2 3]
print(sorted_cols)
