import numpy as np
arr_1 = np.array([[1., 2., 3.], [4., 5., 6.]])
arr_2 = np.array([[7., 8., 9.], [1., 3., 5.]])
print("Original array:\n", arr_1, arr_2)
print("Element-wise addition:\n", arr_1 + arr_2)
print("Element-wise subtraction:\n", arr_1 - arr_2)
print("Element-wise multiplication:\n", arr_1 * arr_2) # np.multiply(arr_1,arr_2)
