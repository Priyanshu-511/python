class A:
    def __init__(self, nums=0):
        self.num = nums

x = A()
print(x.num)
x.num=5
print(x.num)