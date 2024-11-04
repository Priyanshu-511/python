import math

x1 = 1.00
y = float(input("Enter the number: "))
for i in range(10*math.floor(math.log10(y)+1)):
    x2 = ((x1) + (y/x1)) / 2
    x1 = x2

    print(f"calculating....{x2}")

print(f"The square-root of {y} is equal to: {x2}")