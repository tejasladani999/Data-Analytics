# Import libraries
import matplotlib.pyplot as plt
import numpy as np


# Creating dataset
Lastnames = ['Browm', 'Davin', 'Johnson', 
		'Jones', 'Smith', 'willians']

data = [7,6,10,7,12,8]

# Creating plot

plt.pie(data, labels = Lastnames)
plt.title("Most common Last Names in USA")

# show plot
plt.show()
