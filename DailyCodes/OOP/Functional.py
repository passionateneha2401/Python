addition = lambda no1,no2 : (no1+no2)

sub = lambda no1,no2 : (no1-no2)


print("Enter first number : ")
val1 = int(input())

print("Enter second number : ")
val2 = int(input())

ret = addition(val1,val2)
print("addition is : ",ret)

ret = sub(val1,val2)
print("sub is : ",ret)

