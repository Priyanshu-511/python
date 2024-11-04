# n=(input("enter the number: "))
# temp = n
# flag = 1

# for i in range(0,len(n)//2):
#     if n[i] != n[len(n)-1-i]:
#         flag = 0
# if(flag):
#     print("this is palindrome ")

# else:
#     print("this is not palindrome: ")


n = int(input("enter the number: "))
temp = n
sum = 0

for i in range (1,1000):
    term = n%10
    sum = sum*10+term
    if((n//10)==0):
        break

    n=n//10

if(sum == temp):
    print("it is palindrome: ")

else:
    print("it is not a palindrome")