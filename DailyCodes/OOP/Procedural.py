def addition(no1,no2):
    ans = no1 + no2
    return ans

def sub(no1,no2):
    ans = no1 - no2
    return ans

print("Enter first number : ")
val1 = int(input())

print("Enter second number : ")
val2 = int(input())

ret = addition(val1,val2)
print("addition is : ",ret)

ret = sub(val1,val2)
print("sub is : ",ret)
