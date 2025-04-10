import numpy as np  # Importing the NumPy library

# Step 1: Create two 3x3 matrices filled with random integers between 1 and 10
matrix1 = np.random.randint(1, 11, (3, 3))
matrix2 = np.random.randint(1, 11, (3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Step 2: Perform matrix subtraction
subtracted_matrix = matrix1 - matrix2
print("\nMatrix Subtraction (Matrix1 - Matrix2):")
print(subtracted_matrix)

# Step 3: Perform element-wise division, avoiding division by zero
divided_matrix = np.divide(matrix1, matrix2, where=matrix2 != 0)
print("\nElement-wise Division (Matrix1 / Matrix2):")
print(divided_matrix)
