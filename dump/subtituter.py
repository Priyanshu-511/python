a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c,d = a,b
e,f = a,b
g,h = a,b
print(a,b)
print(c,d)
print(e,f)
print("after swapping: ")
a,b = b,a
print(a,b)
c = c^d
d = c^d
c = c^d
print(c,d)
e = e+f
f = e-f
e = e-f
print(e,f)
temp = g
g = h
h = temp
print(g,h)