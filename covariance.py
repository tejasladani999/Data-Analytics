import pandas as pd
import math
df=pd.read_csv("covariance.csv")

mean_x=sum(df['x'])/df.shape[0]
mean_y=sum(df['y'])/df.shape[0]

xi_x=[]
yi_y=[]
sq_xi_x = []
sq_yi_y = []
xi_x_yi_y=[]

for i in range(df.shape[0]):
    xi_x.append(round((df.iat[i,0] - mean_x),2))
    yi_y.append(round((df.iat[i,1] - mean_y),2))
    sq_xi_x.append(round(pow(xi_x[i],2),2))
    sq_yi_y.append(round(pow(yi_y[i],2),2))
    xi_x_yi_y.append(round(((xi_x[i])*(yi_y[i])),2))
    
df['xi-x'] = xi_x
df['yi-y'] = yi_y
df['(xi-x)2']=sq_xi_x
df['(yi-y)2']=sq_yi_y
df['(xi-x)(yi-y)'] = xi_x_yi_y

vx=sum(sq_xi_x)/len(sq_xi_x)
vy=sum(sq_yi_y)/len(sq_yi_y)

sxy=sum(xi_x_yi_y)/len(xi_x_yi_y)
sx=math.sqrt(vx)
sy=math.sqrt(vy)
rxy=round((sxy/(sx*sy)),2)

print("\n",df)
print("\nmean of x =",mean_x)
print("mean of y =",mean_y)
print("\nCovariance =",sxy)
print("Coefficient of correlation =",rxy)