#indexing 
import numpy as np 
arr = np.array([0,1,2,3,4])

print('arr[0] =',arr[0])
print('arr[1] =',arr[1])
print('arr[2] =',arr[2])
print('arr[3] =',arr[3])
print('arr[4] =',arr[4])

#array operations using indexing
print('\nSimple Operations:') 
print('arr[0] + arr[1] =',arr[0]+arr[1])
print('arr[2] - arr[1] =',arr[2]-arr[1])
print('arr[3] * arr[4] =',arr[3]*arr[4])
print('arr[4] / arr[2] =',arr[4]/arr[2])

#access elements in 2D array
arr2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('\n2D array:\n',arr2D)
print('3rd element on 1st array: ', arr2D[0,2])
print('4th element on 2nd array: ', arr2D[1,3])

#access elements in 3D array
arr3D = np.array([[[1,2,3],[4,5,6]],
                  [[7,8,9],[10,11,12]],
                  [[13,14,15],[16,17,18]],
                  [[19,20,21],[22,22,23]]])
print('\n3D array:\n',arr3D)
print('3rd element on 1st array of 2nd array: ', arr3D[1,0,2])
print('1st element on 2nd array of 3rd array: ', arr3D[2,1,0])
print('2nd element on 1st array of 4th array: ', arr3D[3,0,1])

#negative indexing
print('\nUsing negative indexing')
print('From 2D array:')
print('Last element from last array: ', arr2D[-1,-1])
print('From 3D array:')
print('Last element from last array of last array: ', arr3D[-1,-1,-1])
