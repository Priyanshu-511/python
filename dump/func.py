def max(a,b,c):
    if (a>=b and b>=c) or (a>=c and c>=b):
        req = a
    
    elif (b>=c and c>=a) or (b>=a and a>=c):
        req = b
    
    else:
        req = c

    return req

a= input()
b = input()
c = input()

print(max(a,b,c))