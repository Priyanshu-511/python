n = int(input("enter any number: "))

for i in range (n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        if(k%2==0):
            print(" ",end="")
            
        else:
            print("*",end="")
    print()