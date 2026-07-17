'''
2.Write a Python to implement a class named Numbers with following specifications : 
The class should contain 1 instance var:
    Value
Define a constuctor(__init__) that accepts a number from user and initializes Value.
Implement the following instance mthods:
    ChkPrime() - returns true if the number is prime,otherwise returns False.
    ChkPerfect() - returns true if number is perfect, otherwise returns False
    Factors() - displays all factors of number
    SumFactors() - returns sum of all factors.
Create multiple objects and call all methods.
'''
class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if(self.Value <= 1):
            return False

        for i in range(2, self.Value):
            if(self.Value % i == 0):
                return False
        return True

    def ChkPerfect(self):
        total = 0

        for i in range(1, self.Value):
            if(self.Value % i == 0):
                total += i

        if(total == self.Value):
            return True
        else:
            return False

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if(self.Value % i == 0):
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0

        for i in range(1, self.Value + 1):
            if(self.Value % i == 0):
                total += i

        return total


value1 = int(input("Enter first number: "))
obj1 = Numbers(value1)

print("Prime :", obj1.ChkPrime())
print("Perfect :", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors :", obj1.SumFactors())

print()

value2 = int(input("Enter second number: "))
obj2 = Numbers(value2)

print("Prime :", obj2.ChkPrime())
print("Perfect :", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors :", obj2.SumFactors())