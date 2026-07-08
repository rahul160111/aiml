import numpy as np 
arr1 = np.array([[1,2,3],[1,2,3],[1,2,3,]])
print(arr1)
arr2= np.array([[4,5,6],[4,5,6],[4,5,6,]])
print(arr2)

arradd1= arr1 + 2
arradd2 = arr1 + arr2
print('Addition scalar = ', arradd1)
print('Addition matrix =', arradd2)

arrsub2=arr1-arr2
print('sub matrix',arrsub2)

arrdiv2=arr1/arr2
print('div matrix=',arrdiv2)


arrmul = np.matmul(arr1,arr2)
print('mul matrix=',arrmul)

