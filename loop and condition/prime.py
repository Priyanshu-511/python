n = int(input("enter the number: "))
p=0
m=1

for i in range(1,n+1):
    if(n % i)==0 :
        p=p+1

if(p == 2):
    print("it will be prime number: ")
else:
    print("it will be composite number: ")

while(m<=n):
    if(n%m)==0:
        p+=1

    m+=1

if(p==2):
    print("thi is prime number: ")
else:
    print("this is composite number: ")