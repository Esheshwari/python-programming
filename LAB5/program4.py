import numpy as np
array1 = np.array([[0, 1, 2], [2, 3, 4]]) # Manual creation
array2 = np.array( [ [1,2], [3,4] ], dtype=float) # Specifying data type
array3 = np.zeros((2, 3)) # Array of zeros
array4 = np.ones((2, 3)) # Array of ones
array5 = np.eye(3) # Identity matrix
array6 = np.arange(0, 10, 2) # Sequence from 0 to 8 with step 2
array7 = np.linspace(0, 10, 5) # create 5 elements in between 0 to 10 with equal space
array8 = np.random.randint(0, 10, (3, 3)) # Random integers in a 3x3 array
print(array1, "\n")
print(array2, "\n")
print(array3, "\n")
print(array4, "\n")
print(array5, "\n")
print(array6, "\n")
print(array7, "\n")
print(array8, "\n")
