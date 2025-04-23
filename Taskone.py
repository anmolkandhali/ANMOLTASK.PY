import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
average = np.average(temperatures)
print("Average temperature of the week -", average)
highest_temp = temperatures.max()
print("Maximum temperature recorded -", highest_temp)
lowest_temp = temperatures.min()
print("Minimum temperature recorded -", lowest_temp)
fahrenheit = (temperatures * 1.8) + 32
print("Temperatures in Fahrenheit -", fahrenheit)
hot_days = np.where(temperatures > 20)
print("Indexes of days where temperature was above 20°C -",hot_days[0])