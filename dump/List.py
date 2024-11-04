n = input("enter the number: ")

text = list(map(int,n.split()))
fi = int(input("enter finding number: "))
print(text)
print("number of zeroes are:",text.count(fi))

text = sum(text)

print(text)
