import pandas as pd
df=pd.read_csv("data.csv")
print(df)
maxCount=1
for i in range(df.shape[0]):
    curr=df.iat[i,0]
    count=1
    for j in range(i+1, df.shape[0]):
        if(curr==df.iat[j,0]):
            count=count+1
    if(maxCount<=count):
        maxCount=count
        loc=i

print("Mode =",df.iat[loc,0])