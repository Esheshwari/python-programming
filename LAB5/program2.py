import numpy as np
# Creating a 2D NumPy array from a list of lists
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]#no. of sq bracket=no.of dimension
arr2 = np.array(data2)
print("Dimensions:", arr2.ndim) # Output: 2
print("Shape:", arr2.shape) # Output: (2,4)
print(arr2[1])
