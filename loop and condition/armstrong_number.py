n = int(input())
temp=n
sum=0

for i in range (0,1000):
    term = n%10
    sum = sum+term**3

    if(n//10 ==0):
        break

    n=n//10

if(sum == temp):
    print("enter the number is armstrong number: ")

else:
    print("this is not armstrong number: ")