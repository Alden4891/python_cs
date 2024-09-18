# Python Math Cheat Sheet

# ------------------------------
# 1. Importing Math Modules
# ------------------------------

# Import Math Module:
# Comment: Import the built-in math module for mathematical functions.
# Syntax: import math
import math

# Import NumPy Module:
# Comment: Import NumPy for additional mathematical operations.
# Syntax: import numpy as np
import numpy as np

# ------------------------------
# 2. Basic Mathematical Functions
# ------------------------------

# Square Root:
# Comment: Calculate the square root of a number.
# Syntax: math.sqrt(x)
sqrt_value = math.sqrt(16)
print(f"Square Root: {sqrt_value}")

# Exponential:
# Comment: Calculate the exponential of a number.
# Syntax: math.exp(x)
exp_value = math.exp(2)
print(f"Exponential: {exp_value}")

# Logarithm:
# Comment: Calculate the logarithm of a number.
# Syntax: math.log(x, base)
log_value = math.log(100, 10)
print(f"Logarithm (base 10): {log_value}")

# Power:
# Comment: Calculate the power of a number.
# Syntax: math.pow(x, y)
pow_value = math.pow(2, 3)
print(f"Power: {pow_value}")

# Trigonometric Functions:
# Comment: Calculate trigonometric functions (in radians).
# Syntax: math.sin(x), math.cos(x), math.tan(x)
sin_value = math.sin(math.radians(30))
cos_value = math.cos(math.radians(30))
tan_value = math.tan(math.radians(30))
print(f"Sin: {sin_value}, Cos: {cos_value}, Tan: {tan_value}")

# ------------------------------
# 3. Constants
# ------------------------------

# Pi:
# Comment: Get the value of π (pi).
# Syntax: math.pi
pi_value = math.pi
print(f"Pi: {pi_value}")

# Euler's Number:
# Comment: Get the value of e (Euler's number).
# Syntax: math.e
e_value = math.e
print(f"Euler's Number: {e_value}")

# ------------------------------
# 4. NumPy Mathematical Functions
# ------------------------------

# Square Root:
# Comment: Calculate the square root of an array.
# Syntax: np.sqrt(array)
sqrt_array = np.sqrt([1, 4, 9, 16])
print(f"NumPy Square Roots: {sqrt_array}")

# Exponential:
# Comment: Calculate the exponential of an array.
# Syntax: np.exp(array)
exp_array = np.exp([1, 2, 3])
print(f"NumPy Exponential: {exp_array}")

# Logarithm:
# Comment: Calculate the logarithm of an array.
# Syntax: np.log(array)
log_array = np.log([1, np.e, np.e**2])
print(f"NumPy Logarithm: {log_array}")

# Power:
# Comment: Calculate the power of an array.
# Syntax: np.power(array, exponent)
pow_array = np.power([1, 2, 3], 2)
print(f"NumPy Power: {pow_array}")

# Trigonometric Functions:
# Comment: Calculate trigonometric functions for an array (in radians).
# Syntax: np.sin(array), np.cos(array), np.tan(array)
radians_array = np.radians([30, 45, 60])
sin_array = np.sin(radians_array)
cos_array = np.cos(radians_array)
tan_array = np.tan(radians_array)
print(f"NumPy Sin: {sin_array}, Cos: {cos_array}, Tan: {tan_array}")

# ------------------------------
# 5. Array Operations
# ------------------------------

# Element-wise Operations:
# Comment: Perform element-wise operations on arrays.
# Syntax: np.add(array1, array2), np.subtract(array1, array2)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
sum_array = np.add(array1, array2)
diff_array = np.subtract(array1, array2)
print(f"Sum: {sum_array}, Difference: {diff_array}")

# Statistical Operations:
# Comment: Perform statistical operations on arrays.
# Syntax: np.mean(array), np.median(array), np.std(array)
mean_value = np.mean(array1)
median_value = np.median(array1)
std_dev_value = np.std(array1)
print(f"Mean: {mean_value}, Median: {median_value}, Std Dev: {std_dev_value}")

# ------------------------------
# 6. Advanced Mathematical Functions
# ------------------------------

# Gamma Function:
# Comment: Calculate the gamma function of a number.
# Syntax: math.gamma(x)
gamma_value = math.gamma(5)
print(f"Gamma Function: {gamma_value}")

# Factorial:
# Comment: Calculate the factorial of a number.
# Syntax: math.factorial(x)
factorial_value = math.factorial(5)
print(f"Factorial: {factorial_value}")

# ------------------------------
# 7. Random Number Generation
# ------------------------------

# Random Integer:
# Comment: Generate a random integer between low and high.
# Syntax: np.random.randint(low, high)
random_int = np.random.randint(1, 10)
print(f"Random Integer: {random_int}")

# Random Float:
# Comment: Generate a random float between 0 and 1.
# Syntax: np.random.random()
random_float = np.random.random()
print(f"Random Float: {random_float}")

# ------------------------------
# 8. Linear Algebra
# ------------------------------

# Matrix Multiplication:
# Comment: Perform matrix multiplication.
# Syntax: np.dot(matrix1, matrix2)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)
print(f"Matrix Product:\n{matrix_product}")

# Determinant:
# Comment: Calculate the determinant of a matrix.
# Syntax: np.linalg.det(matrix)
determinant = np.linalg.det(matrix1)
print(f"Determinant: {determinant}")

# Inverse:
# Comment: Calculate the inverse of a matrix.
# Syntax: np.linalg.inv(matrix)
inverse_matrix = np.linalg.inv(matrix1)
print(f"Inverse Matrix:\n{inverse_matrix}")
