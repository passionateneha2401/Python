'''
3.Write a Python program to implement a class named Arithmetic with following specifications : 
The class should contain 2 instance var : Value1 and Value2.
Define contructor (__init__) that initiales all instance var to 0.0.
Implement two instance methods : 
    Accept() - accepts value1 and value2 from the user.
    Addition() - returns addition
    Substraction()
    Multiplication()
    Division()-handle division by zero properly.

Create multiple objects of the Arithmectic class and imvoke all instance methods for each object.
'''

class Arithmetic:
    def __init__(self):
        self.Value1 = 0.0
        self.Value2 = 0.0

    def Accept(self):
        self.Value1 = float(input("Enter value1 : "))
        self.Value2 = float(input("Enter value2 : "))

    def Addition(self):
        ans = self.Value1 + self.Value2
        return ans
  
    def Substraction(self):
        ans = self.Value1 - self.Value2
        return ans
    
    def Multiplication(self):
        ans = self.Value1 * self.Value2
        return ans

    def Division(self):
        try:
            ans = self.Value1 / self.Value2
            return ans
        except ZeroDivisionError as zobj:
            print("exception occured due to second operand is zero : ",zobj)
  


obj1 = Arithmetic()
obj2 = Arithmetic()

obj1.Accept()

ret = obj1.Addition()        
print("add is : ",ret)

ret = obj1.Substraction()        
print("sub is : ",ret)

ret = obj1.Multiplication()        
print("multiplication is : ",ret)

ret = obj1.Division()        
if(ret != None):
    print("Division is : ",ret)

obj2.Accept()

ret = obj2.Addition()        
print("add is : ",ret)

ret = obj2.Substraction()        
print("sub is : ",ret)

ret = obj2.Multiplication()        
print("multiplication is : ",ret)

ret = obj2.Division()        
if(ret != None):
    print("Division is : ",ret)
