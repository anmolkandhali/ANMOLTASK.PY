import numpy as np
numbers = np.array([i for i in range(1, 11)])
print("Original Array -", numbers)
array_shape = numbers.shape
array_type = numbers.dtype
print("shape -", array_shape)
print("Data Type -", array_type)
multiplied = numbers * 2
print("Multiply -", multiplied)