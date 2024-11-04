import numpy as np

a = np.array([1,2,3,4,5])
b = a.copy()
c= a.view()

print(a)
print(b)
print(c)

print()
print()


a[3] =7

print(a)
print(b)
print(c)

a = b.view()

print()
print()

print(a)
print(b)
print(c)
