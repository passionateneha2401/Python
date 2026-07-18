class Demo:
    def __init__(self,A):
        self.no = A

    def __add__(self, other):
        return self.no + other.no
    
    def __sub__(self, other):
        return self.no - other.no
    
    def __mul__(self, other):
        return self.no * other.no
    
    def __truediv__(self, other):
        return self.no / other.no
    


obj1 = Demo(11)
obj2 = Demo(21)

print("addition is: ",obj1+obj2)       #obj1.__add__(obj2) --> __add__(obj1,obj2) 
print("sub is: ",obj1-obj2) 
print("mul is: ",obj1*obj2) 
print("div is: ",obj1/obj2) #obj1.__truediv__(obj2) --> __truediv__(obj1,obj2) 


