import numpy as np

#simple tuple 
arrTuple = np.array((1,2,3,4,5))
print('Simple NumPy array using tuple: ',arrTuple)

#0-D Array
arr0 = np.array(0)
print('\n0-D array: ',arr0)

#1-D Array
arr1 = np.array([0,1])
print('\n1-D array: ',arr1)

#2-D Array
arr2a = np.array([[0,1],[2,3]])
print('\n2-D array:\n',arr2a)

arr2b = np.array([[0,1],['a','b']])
print('\n2-D array:\n',arr2b)

#3-D Array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('\n3-D array:\n',arr3)

#dimensions of the arrays
print("dimensions of arrTuple: ", arrTuple.ndim)
print("dimensions of arr0:     ", arr0.ndim)
print("dimensions of arr1:     ", arr1.ndim)
print("dimensions of arr2a:    ", arr2a.ndim)
print("dimensions of arr2b:    ", arr2b.ndim)
print("dimensions of arr3:     ", arr3.ndim)

#create an array with n dimensions
print('\nArray with n dimensions')
n = 5 
arrDim1 = np.array([1,2,3,4],ndmin=n)
print(n,'-D array:\n', arrDim1)
print('number of dimensions :', arrDim1.ndim)

print()
n = 10
arrDim2 = np.array([1,2,3,4],ndmin=n)
print(n,'-D array:\n', arrDim2)
print('number of dimensions :', arrDim2.ndim)
