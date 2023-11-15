# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
a = [187,175,165,162,172,184,172,208,172,175,174,202,
     215,182,170,185,197,164,156,183]

# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(a, bins = [150, 160, 170, 180, 190, 200,210])

# Show plot
plt.xlabel("Annual base salary ($1000)")
plt.ylabel("superintendents")
plt.title("Candidate Salaries distribution")
plt.show()