import numpy as np

array_size = 12
random_array = np.random.randint(0, 10, size=array_size)

mean_value = np.mean(random_array)
std_dev_value = np.std(random_array)

reshaped_array = random_array.reshape(3, 4)

print("Random Array:")
print(random_array)
print("\nMean:", mean_value)
print("Standard Deviation:", std_dev_value)
print("\nReshaped Array (3x4):")
print(reshaped_array)
