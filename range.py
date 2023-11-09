import math
import pandas as pd

data = [12,11,4,2,32,12,45,32,-101,150]
r= max(data)- min(data)

df = pd.DataFrame(data,columns=['x'])
print(df)
print("Range =", r)
