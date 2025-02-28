import numpy as np
# Creating a 1D NumPy array
data1 = [1, 7, 5, 8, 0, 1] #it is a list
arr1 = np.array(data1) # list --> converts to ndarray
print(arr1) # [6 7 5 8 0 1]
print("Type:",type(arr1)) # Type: <class 'numpy.ndarray'>
print("Shape:", arr1.shape) # Shape: (6,)#for 1-d it only prints cols
print("Size:",arr1.size) # Size: 6
print("Dimensions:", arr1.ndim) # Dimensions: 1
print("Data type:", arr1.dtype) # Data type: int64
print("Item_Size:",arr1.itemsize) # size in bytes of each element of the array.
print("total_memory: =", arr1.size * arr1.itemsize,"bytes")
# Convert the list into a NumPy array
array_1 = [1, 2, 3, "RV"]
arr_1_np = np.array(array_1)  # Convert list to NumPy array

# Print the NumPy array and its data type
print(arr_1_np)
print("Data type:", arr_1_np.dtype)  # Access dtype of the NumPy array
array_2=[1,2,3,4,'A']
print(array_2)
