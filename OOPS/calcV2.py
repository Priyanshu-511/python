import math

class calculator:
    @staticmethod
    def sqrt(self,num=5):
        return math.sqrt(num)
    
    def sqre(self,num):
        return num**2
    
    def cube(self,num):
        return num**3
    

a = calculator()
print(a.cube(5),a.sqre(5),a.sqrt(5))