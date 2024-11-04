import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
b= a.reshape(3,4)
print(b)
c = a.reshape(6,2)
print(c)
d= a.reshape(2,2,3)
print(d)

x = np.array([1,2,3,4,5])
y = np.array([8,9,0])
z = np.concatenate((x,y))
print(z)

e = np.array_split(a,5)
print(e)

f=np.where(a%3==0)
print (f)

