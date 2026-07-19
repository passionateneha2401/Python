class Arithematic:
    def addition(no1,no2):
        ans = no1 + no2
        return ans

    def sub(no1,no2):
        ans = no1 - no2
        return ans
    
Aobj = Arithematic()

print("Enter first number : ")
val1 = int(input())

print("Enter second number : ")
val2 = int(input())

ret = Aobj.addition(val1,val2)   #ret = addition(Aobj,val1,val2)
print("addition is : ",ret)

ret = Aobj.sub(val1,val2)        #error
print("sub is : ",ret)
