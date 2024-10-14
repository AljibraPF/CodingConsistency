#Playing with Numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean_value = np.mean(arr)
print("Mean:", mean_value)

sum_value = np.sum(arr)
print("Sum:", sum_value)

max_value = np.max(arr)
print("Maximum:", max_value)

reshaped_arr = arr.reshape(2, 5)
print("Reshaped array:\n", reshaped_arr)

#Real life example of it being used

temperatures = np.array([22, 25, 23, 20, 24, 26, 21])

average_temp = np.mean(temperatures)
print(f"Average temp: {average_temp:.2f}°C")

hottest_temp = np.max(temperatures)
print(f"Hottest temp: {hottest_temp}°C")

coldest_temp = np.min(temperatures)
print(f"Coldest temp: {coldest_temp}°C")