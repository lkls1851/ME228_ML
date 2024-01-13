import numpy as np
import pandas as pd

data={'one':[1 for i in range(10)],
        'd':[10,15,20,25,30,35,40,45,50,55]}

df=pd.DataFrame(data)
arr=df[['one','d']].values

arr=np.power(arr, -0.5)
arrt=np.transpose(arr)

a=np.matmul(arrt, arr)


sigma=np.array([[65],[55.5],[52],[48],[46],[43],[42.5],[40.5],[40],[38]])

xt=np.matmul(arrt, sigma)
x=np.linalg.solve(a, xt)



print(f"The value of sigma_c is {int(x[0][0])} and value of k is {int(x[1][0])}")

