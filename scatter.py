# Import libraries
import matplotlib.pyplot as plt
import numpy as np

x = [30,50,40,55,30,25,60,25,50,55]
y = [28,25,25,23,30,32,21,35,26,25]

plt.xlabel("Driving Speed")
plt.ylabel("Miles per Gallon")
plt.title("Study on Automobiles")
plt.scatter(x, y)
plt.show()

