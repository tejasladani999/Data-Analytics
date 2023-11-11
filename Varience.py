import math
#import statistics
import pandas as pd

data = [28,42,58,48,45,55,60,49,50]

df = pd.DataFrame(data,columns=['x'])
M = (round((sum(data)/len(data)),2))
xi_x = []
sq_xi_x = []


for i in range(df.shape[0]):
    xi_x.append(round((df.iat[i,0]-M),2))
    sq_xi_x.append(round(pow(xi_x[i],2),2))
    
df['xi-x'] = xi_x    
df['(xi-x)2']=sq_xi_x

variance=(round(sum(sq_xi_x)/len(sq_xi_x),2))
std_dev=(round(math.sqrt(variance),2))
co=(round(((std_dev/M)*100),2))

print('\n',df)
print("\nmean =",M)
print("variance =",variance)
print("standard deviation =",std_dev)
print("coefficient of variation =",co,"%")