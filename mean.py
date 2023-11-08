import pandas as pd 

df=pd.read_csv("data.csv")
print(df)
sum=0
print("n=",df.shape[0])
for i in range(df.shape[0]):  #for(int i=0;i<df.shape[0];i++)
   sum=sum + df.iat[i,0]

print("mean =",sum/df.shape[0])

