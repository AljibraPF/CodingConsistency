#Playing with Numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean_value = np.mean(arr)
print("Mean of the array:", mean_value)

sum_value = np.sum(arr)
print("Sum of the array:", sum_value)

max_value = np.max(arr)
print("Maximum value in the array:", max_value)

reshaped_arr = arr.reshape(2, 5)
print("Reshaped array:\n", reshaped_arr)
