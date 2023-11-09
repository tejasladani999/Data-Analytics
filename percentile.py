import pandas as pd
df = pd.read_csv("data.csv")

df=df.sort_values(by="xi")
print(df)
p=input("Enter percentile: ")

i = ( (int(p)/100)*(df.shape[0]) )
Qp=0
if i % 1 != 0:
   i=int(i)
   Qp=df.iat[i,0]
else:
  i=int(i)
  Qp=((df.iat[i,0]+df.iat[i-1,0])/2)

  
print(p,"th percentile =",Qp)