import numpy as np
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print("Element-wise addition:\n", arr + 2)
print("Element-wise multiplication:\n", arr * 2)
print("Element-wise exponentiation:\n", arr ** 2)
print("Comparison:\n", arr2 > arr)
