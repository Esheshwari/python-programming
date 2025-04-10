import numpy as np  # Importing NumPy library

# Step 1: Create a 3x3 NumPy array filled with random integers between 1 and 20
array = np.random.randint(1, 21, (3, 3))
print("Original 3x3 Array:")
print(array)

# Step 2: Calculate the mean of the array
mean_value = np.mean(array)
print(f"\nMean of the array: {mean_value}")

# Step 3: Replace all elements less than 10 with 0
modified_array = np.where(array < 10, 0, array)
print("\nModified Array (with elements < 10 replaced by 0):")
print(modified_array)
