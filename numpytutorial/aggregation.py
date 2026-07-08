import numpy as np 
l = [1,2,3,4,5,6,7,-9-7-5]
a = np.array(l,ndmin=4)
print(a) 
print(a.shape)
print(a.ndim)
minimum = a.min()
print(minimum)

argmini = a.argmin()
print(argmini)

argmax =a.argmax()
print(argmax)

add = a.sum()
print(add)

mean = a.mean()
print(mean)

s =a.std()
print(s)

array2d =np.array([[1,2,3,],[4,5,6],[7,8,9]])
add1 = array2d.sum(axis=0) #axis 0 is used for coloumn add 
print(array2d)
print(add1)

array2d =np.array([[1,2,3,],[4,5,6],[7,8,9]])
add1 = array2d.sum(axis=1) #axis 1 is used for row total count 
print(array2d)
print(add1)
