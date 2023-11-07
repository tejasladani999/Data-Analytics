import pandas as pd 

data=[14,20,23,16,17,16,22,12,
      19,24,25,15,23,19,22,25,
      24,20,25,24,26,21,16,19,
      19,21,19,24,22,23,16,24,
      16,22,18,18,21,20,16,20]

# print(data)

df = pd.Series(data).value_counts(sort=True)
print("\n frequancy: ")
print(df)
print("\n Relative frequancy: ")
print(df/len(data))
print("\n Petcantage frequancy: ")
print((df/len(data))*100 )