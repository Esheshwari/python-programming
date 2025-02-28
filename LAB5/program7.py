# Create a 2D array
import numpy as np
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print("Original Array:\n", arr)
# Slice the first row
row_slice = arr[1:, 2:] # Equivalent to arr[0]
# Slice the second column
col_slice = arr[:3, ]
# Slice a submatrix (rows 1-2, columns 2-3) to get 7,8,11,12
submatrix = arr[1:3, 2:4]
print("\nFirst Row:", row_slice)
print("Second Column:", col_slice)
print("Submatrix:\n", submatrix)
