import numpy as np 
a = np.array([2,4,6,8,1,3,-8])
print(f"befor sort:{a}")
a.sort()
print(f"after sort:{a}")

dt = np.dtype([('name','S10'),('age',int)])
b = np.array([('rahul',20),('ABC',30),('XYZ',10)], dtype=dt)
b.sort(order='name')
print(b)

