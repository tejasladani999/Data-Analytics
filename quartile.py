import pandas as pd
import math
df = pd.read_csv("Iqr.csv")

#only for dataframe by column name

df = df.sort_values(by='x')
print("\nDataset after arrange in ascending Order")
print(df)
length = df.shape[0]

print("\nno. of element =",length)

i1 = (25/100) * length
i2= (50/100) * length
i3 = (75/100) * length

if i1%1==0:
    i1 =  int(i1)
    q1 = (df.iat[i1-1, 0] + df.iat[i1, 0])/2
else:
    i1 = int(math.ceil(i1))
    q1 = df.iat[i1-1, 0]

if i2%1==0:
    i2 = int(i2)
    q2 = (df.iat[i2-1, 0] + df.iat[i2, 0])/2
else:
    i2 = int(math.ceil(i2))
    q2 = df.iat[i2-1, 0]
   
if i3%1==0:
    i3 = int(i3)
    q3 = (df.iat[i3-1, 0] + df.iat[i3, 0])/2
else:
    i3 = int(math.ceil(i3))
    q3 = df.iat[i3-1, 0]
   
print("Q1 position =",i1)
print("Q2 position =",i2)
print("Q1 position =",i3)

print("Q1 =",q1)
print("Q2 =",q2)
print("Q3 =",q3)