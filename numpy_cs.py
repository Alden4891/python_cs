# NumPy Cheat Sheet

# ------------------------------
# 1. Installing NumPy
# ------------------------------

# Install NumPy Package:
# Comment: Install the NumPy library from PyPI.
# Syntax: pip install numpy
pip install numpy

# ------------------------------
# 2. Importing NumPy
# ------------------------------

# Import NumPy:
# Comment: Import the entire NumPy library.
# Syntax: import numpy as alias
import numpy as np


# ------------------------------
# 3. Creating Arrays
# ------------------------------

# Creating an Array:
# Comment: Create a NumPy array from a list.
# Syntax: np.array([elements])
arr = np.array([1, 2, 3, 4, 5])

# Creating a 2D Array:
# Comment: Create a 2D NumPy array (matrix).
# Syntax: np.array([[row1], [row2], ...])
matrix = np.array([[1, 2], [3, 4]])

# Creating Arrays of Zeros:
# Comment: Create an array filled with zeros.
# Syntax: np.zeros(shape)
zeros_arr = np.zeros((2, 3))

# Creating Arrays of Ones:
# Comment: Create an array filled with ones.
# Syntax: np.ones(shape)
ones_arr = np.ones((2, 3))

# Creating Arrays with a Range of Values:
# Comment: Create an array with values in a range.
# Syntax: np.arange(start, stop, step)
range_arr = np.arange(0, 10, 2)

# Creating Linearly Spaced Values:
# Comment: Create an array with linearly spaced values.
# Syntax: np.linspace(start, stop, num)
linspace_arr = np.linspace(0, 1, 5)


# ------------------------------
# 4. Array Operations
# ------------------------------

# Element-wise Addition:
# Comment: Add two arrays element-wise.
# Syntax: arr1 + arr2
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr = arr1 + arr2

# Element-wise Multiplication:
# Comment: Multiply two arrays element-wise.
# Syntax: arr1 * arr2
product_arr = arr1 * arr2

# Dot Product:
# Comment: Compute the dot product of two arrays.
# Syntax: np.dot(arr1, arr2)
dot_product = np.dot(arr1, arr2)

# Matrix Multiplication:
# Comment: Perform matrix multiplication.
# Syntax: np.matmul(matrix1, matrix2)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.matmul(matrix1, matrix2)


# ------------------------------
# 5. Array Indexing and Slicing
# ------------------------------

# Accessing an Element:
# Comment: Access an element by its index.
# Syntax: arr[index]
element = arr1[0]

# Slicing an Array:
# Comment: Extract a subarray by slicing.
# Syntax: arr[start:stop:step]
sub_arr = arr1[0:3]

# Accessing Elements in a 2D Array:
# Comment: Access an element in a 2D array.
# Syntax: matrix[row, col]
element_2d = matrix[0, 1]

# Slicing a 2D Array:
# Comment: Slice a 2D array to extract subarrays.
# Syntax: matrix[start_row:end_row, start_col:end_col]
sub_matrix = matrix1[0:2, 1:2]


# ------------------------------
# 6. Reshaping Arrays
# ------------------------------

# Reshaping an Array:
# Comment: Reshape an array to a different shape.
# Syntax: arr.reshape(new_shape)
reshaped_arr = arr1.reshape((3, 1))

# Flattening a 2D Array:
# Comment: Flatten a 2D array into 1D.
# Syntax: arr.flatten()
flattened_matrix = matrix1.flatten()


# ------------------------------
# 7. Mathematical Functions
# ------------------------------

# Sum of Elements:
# Comment: Compute the sum of array elements.
# Syntax: np.sum(arr)
sum_elements = np.sum(arr1)

# Mean of Elements:
# Comment: Compute the mean of array elements.
# Syntax: np.mean(arr)
mean_elements = np.mean(arr1)

# Standard Deviation:
# Comment: Compute the standard deviation of array elements.
# Syntax: np.std(arr)
std_elements = np.std(arr1)

# Maximum and Minimum:
# Comment: Find the maximum and minimum elements.
# Syntax: np.max(arr), np.min(arr)
max_element = np.max(arr1)
min_element = np.min(arr1)

# Exponentiation and Logarithms:
# Comment: Perform element-wise exponentiation and logarithms.
# Syntax: np.exp(arr), np.log(arr)
exp_arr = np.exp(arr1)
log_arr = np.log(arr1)


# ------------------------------
# 8. Random Number Generation
# ------------------------------

# Random Numbers from Uniform Distribution:
# Comment: Generate random numbers from a uniform distribution.
# Syntax: np.random.rand(shape)
random_uniform = np.random.rand(3)

# Random Integers:
# Comment: Generate random integers within a range.
# Syntax: np.random.randint(low, high, size)
random_integers = np.random.randint(0, 10, size=5)

# Random Numbers from Normal Distribution:
# Comment: Generate random numbers from a normal distribution.
# Syntax: np.random.randn(shape)
random_normal = np.random.randn(3)


# ------------------------------
# 9. Boolean Indexing
# ------------------------------

# Boolean Masking:
# Comment: Use conditions to filter an array.
# Syntax: arr[condition]
mask = arr1 > 2
filtered_arr = arr1[mask]

# ------------------------------
# 10. Broadcasting
# ------------------------------

# Adding a Scalar to an Array:
# Comment: Add a scalar to every element of an array.
# Syntax: arr + scalar
arr_with_scalar = arr1 + 10

# Broadcasting in Arithmetic:
# Comment: Perform arithmetic operations with broadcasting.
# Syntax: arr1 * arr2 (with different shapes)
broadcasted_result = arr1 * np.array([[1], [2], [3]])

# ------------------------------
# 11. Saving and Loading Data
# ------------------------------

# Save Array to File:
# Comment: Save an array to a binary .npy file.
# Syntax: np.save("filename.npy", arr)
np.save("array_file.npy", arr1)

# Load Array from File:
# Comment: Load an array from a .npy file.
# Syntax: np.load("filename.npy")
loaded_arr = np.load("array_file.npy")

# Save Array to Text File:
# Comment: Save an array to a .txt file.
# Syntax: np.savetxt("filename.txt", arr)
np.savetxt("array_file.txt", arr1)

# Load Array from Text File:
# Comment: Load an array from a .txt file.
# Syntax: np.loadtxt("filename.txt")
loaded_txt_arr = np.loadtxt("array_file.txt")

