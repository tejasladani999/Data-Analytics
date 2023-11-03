# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

sample = [12,11,4,2,32,12,45,32, 50,-55,108]
#plt.figure(figsize=(10, 10))

# creating the box plot

plt.boxplot(sample,vert=True)
plt.ylabel('Sample')
#plt.boxplot(sample,vert=False)
#plt.xlabel('Sample')
plt.title("Detecting outliers using Boxplot")

# showing ploting
plt.show()