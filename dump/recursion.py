def fact(n):
    if n==0 or n==1:
        return 1
    
    else:
        return n*fact(n-1)
    

def dearrangement(n):
    if n==0 or n==2:
        return 1
    
    elif n==1:
        return 0
    
    else:
        return (dearrangement(n-1)+dearrangement(n-2))*(n-1)
    

print(fact(5))
print(dearrangement(6))