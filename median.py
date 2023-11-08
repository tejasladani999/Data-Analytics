import pandas as pd 

df=pd.read_csv("data.csv")

df=df.sort_values(by='xi')
print(df)
if df.shape[0] % 2 == 0 :
    print("even")
    i=int(df.shape[0]/2)
    mid=((df.iat[i,0]+df.iat[i-1,0])/2)
else:
    i=int(df.shape[0]/2)
    mid=df.iat[i,0]

print("median =",mid)