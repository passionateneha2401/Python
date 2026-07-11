class Arithematic:
    #parametrized consturctor
    #specialmethod -- constructor
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def addition(self):
        ans = self.no1 + self.no2
        return ans

    def sub(self):
        ans = self.no1 - self.no2
        return ans
    
Aobj = Arithematic()

print("Enter first number : ")
val1 = int(input())

print("Enter second number : ")
val2 = int(input())
    
Aobj = Arithematic(val1,val2)

ret = Aobj.addition()   #ret = addition(Aobj,val1,val2)
print("addition is : ",ret)

ret = Aobj.sub()        
print("sub is : ",ret)
