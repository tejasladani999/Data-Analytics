# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = [1,3,7,5,1,2,1]
range = [150, 160, 170, 180, 190, 200,210]

df = pd.DataFrame(list(data),index=range,columns=['data'])
#lineStype or ls use form dotted or desshed style
plt.title("Candidate Salaries distribution")
plt.ylabel("superintendents")
plt.xlabel("Annual base salary ($1000)")
plt.plot(df)
plt.show()