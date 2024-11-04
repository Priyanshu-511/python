n = int(input("Enter the number: "))

for i in range(0,n):
    if i == 0 or i == n-1:
        for j in range(n):
            print("* ",end="")

    else:
        for j in range(n):
            if j ==0 or j==n-1 :
                print("* ",end="")

            else:
                print("  ",end="")
    
    print()