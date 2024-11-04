def cel(temp):
    celcius = (5/9*(temp-32))
    return celcius

def fah(temp):
    fahrenheit = ((9/5*temp)+32)
    return fahrenheit

def kel(temp):
    req = cel(temp)
    kelvin = req+273.15
    return kelvin

temp = float(input("Enter the temp: "))
print("in fahrenheit:",fah(temp))
print("in celcius:",cel(temp))
print("in kelvin:",kel(temp))