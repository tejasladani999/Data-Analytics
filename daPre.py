# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("titanic.csv")

#print(df)

# to remove null values
titanicDf = df["body"].dropna()
#print(titanicDf)

# to remove null values
titanicDf = df.dropna(subset=['body'])
#print(titanicDf)

#Get dimension of the df
#print(df.shape)
#print(titanicDf.shape)
#

#print(titanicDf.shape[0])
#print(titanicDf.shape[1])


#remove columns
df1 = df.drop(['body'], axis=1)
#print(df1.shape[1])


#df1 = df.drop(['body','survived'], axis=1)
#print(df1.shape[1])

#print(df1)

# rename
df1.rename(columns={'survived': 'alive'}, inplace=True)
#print(df1)


# Change the case

#print(df1['home.dest'].str.upper())
#print(df1['home.dest'].str.lower())
#print(df1['home.dest'].str.capitalize())
#df1['home.dest'] = df1['home.dest'].str.upper()
#print(df1) 
#null values 

#print(df.isnull())
#print(df.isnull().sum())
#print(df.isnull().sum().sum())


#        Dealing with missing values
#print(df)

#df['body'] = df['body'].fillna(0)
#print(df)


#df['body'] = df['body'].fillna(df['body'].mean())
#print(df)


#df['body'] = df['body'].fillna(df['body'].median())
#print(df)

#print(df)
#df['body'] = df['body'].fillna(df['body'].mode())
#print(df)

#print(df)
#
#df['body'] = df['body'].fillna(method='bfill')
#print(df)
#    

#df['body'] = df['body'].fillna(method='ffill')
#print(df)



#         unique values
#df3 = pd.read_csv("hello.csv")
#print(df3)
#print(df3["classed"].unique())







