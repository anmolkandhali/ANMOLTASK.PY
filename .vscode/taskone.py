# Step 1: Import NumPy

import numpy as np

# Step 2: Store weekly temperatures in a NumPy array

temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# Step 3: Calculate the average temperature using np.average()

average = np.average(temperatures)
print("Average temperature of the week -", average)

# Step 4: Get the maximum temperature using .max() method

highest_temp = temperatures.max()
print("Maximum temperature recorded -", highest_temp)

# Step 5: Get the minimum temperature using .min() method

lowest_temp = temperatures.min()
print("Minimum temperature recorded -", lowest_temp)

# Step 6: Convert all temperatures to Fahrenheit using formula

fahrenheit = (temperatures * 1.8) + 32
print("Temperatures in Fahrenheit -", fahrenheit)

# Step 7: Find indices where temperature is above 20°C

hot_days = np.where(temperatures > 20)
print("Indexes of days where temperature was above 20°C -",hot_days[0])