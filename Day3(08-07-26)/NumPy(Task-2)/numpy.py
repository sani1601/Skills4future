import numpy as np

# 1. Create a multidimensional array (2D array for demonstration)
print("1. Creating a 2D NumPy array:")
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print(arr)
print("-" * 30)

# 2. Use index numbers to access values
print("2. Accessing values using index numbers:")
value_at_0_0 = arr[0, 0]
value_at_1_2 = arr[1, 2]
print(f"Value at (0, 0): {value_at_0_0}")
print(f"Value at (1, 2): {value_at_1_2}")
print(f"Row 0: {arr[0, :]}")
print(f"Column 3: {arr[:, 3]}")
print("-" * 30)

# 3. Perform mathematical operations on accessed values
print("3. Performing mathematical operations on accessed values:")
result_sum = arr[0, 0] + arr[1, 2]
result_product = arr[2, 1] * arr[0, 3]
print(f"Sum of arr[0,0] and arr[1,2]: {result_sum}")
print(f"Product of arr[2,1] and arr[0,3]: {result_product}")
print("-" * 30)

# 4. Apply at least 15 NumPy methods on arrays

print("4. Applying NumPy methods:")

# Method 1: shape - Get the dimensions of the array
print(f"  Method 1 (shape): Array shape: {arr.shape}")

# Method 2: ndim - Get the number of dimensions
print(f"  Method 2 (ndim): Number of dimensions: {arr.ndim}")

# Method 3: size - Get the total number of elements
print(f"  Method 3 (size): Total elements: {arr.size}")

# Method 4: dtype - Get the data type of elements
print(f"  Method 4 (dtype): Data type: {arr.dtype}")

# Method 5: sum() - Sum of all elements
print(f"  Method 5 (sum): Sum of all elements: {arr.sum()}")

# Method 6: sum(axis=0) - Sum along columns
print(f"  Method 6 (sum(axis=0)): Sum along columns: {arr.sum(axis=0)}")

# Method 7: mean() - Mean of all elements
print(f"  Method 7 (mean): Mean of all elements: {arr.mean()}")

# Method 8: max() - Maximum element
print(f"  Method 8 (max): Maximum element: {arr.max()}")

# Method 9: min() - Minimum element
print(f"  Method 9 (min): Minimum element: {arr.min()}")

# Method 10: std() - Standard deviation
print(f"  Method 10 (std): Standard deviation: {arr.std():.2f}") # Formatted to 2 decimal places

# Method 11: reshape() - Change array shape
reshaped_arr = arr.reshape(2, 6) # Original 3x4 = 12 elements. Reshape to 2x6.
print(f"  Method 11 (reshape): Reshaped array (2x6):\n{reshaped_arr}")

# Method 12: transpose() - Transpose the array
transposed_arr = arr.transpose()
print(f"  Method 12 (transpose): Transposed array:\n{transposed_arr}")

# Method 13: flatten() - Flatten the array to 1D
flattened_arr = arr.flatten()
print(f"  Method 13 (flatten): Flattened array: {flattened_arr}")

# Method 14: argmax() - Index of the maximum value along an axis
print(f"  Method 14 (argmax(axis=1)): Index of max value per row: {arr.argmax(axis=1)}")

# Method 15: argmin() - Index of the minimum value along an axis
print(f"  Method 15 (argmin(axis=0)): Index of min value per column: {arr.argmin(axis=0)}")

# Method 16: np.sqrt() - Square root of each element (universal function)
print(f"  Method 16 (np.sqrt): Square root of array elements (first 2 rows):\n{np.sqrt(arr[:2,:])}")

# Method 17: np.add() - Element-wise addition (universal function)
arr2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
added_arr = np.add(arr, arr2)
print(f"  Method 17 (np.add): Element-wise addition with another array:\n{added_arr}")

print("-" * 30)
