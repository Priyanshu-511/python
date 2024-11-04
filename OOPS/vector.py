class one_dim:
    def __init__(self):
        return 0
    
    def __init__(self,x):
        self.x = x

class two_dim(one_dim):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

class three_dim(two_dim):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

m=one_dim(5)
print(m.x)
n=two_dim(5,6)
print(n.x,n.y)
o=three_dim(5,6,7)
print(o.x,o.y,o.z)