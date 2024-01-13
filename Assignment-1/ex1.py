import numpy as np
v=np.array([[1,-1,1],[1,2,4],[1,1,1]])
f=np.array([[6],[9],[2]])
a=np.linalg.solve(v,f)
print(f"The coefficient a0 is {int(a[0][0])}, a1 is {int(a[1][0])}, a2 is {int(a[2][0])}")
