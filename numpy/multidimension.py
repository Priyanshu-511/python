import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
print("its dimension is", arr.ndim)

arr2 = np.array([[[1,2,3],[4,5,6]],[[4,3,6],[8,9,0]]])

print(arr2)
print(arr2.ndim)