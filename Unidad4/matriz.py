import numpy as np

mat = np.array([4,8,2])
print(mat)
print(type(mat))

mat2 = np.array([[5,8,7],[3,5,9]])
print(mat2)
print(type(mat2[0][2]))
mat2[0][0] = 1582
print(mat2)

mat3= np.array([[[8,9,5],[6,8,4],[6,1,2]],[[8,2,5],[9,9,4],[2,2,1]]])
print(mat3)
print(mat3.shape)