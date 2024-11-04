class Programmer:
    company="microsoft"
    def name(self,name,salary):
        print(f"Name:-{name}")
        print(f"Salary is ${salary}")

a=Programmer()
print("Name of company is:",a.company)
a.name("NOD",500000)
print()
a.name("donald",300000)
