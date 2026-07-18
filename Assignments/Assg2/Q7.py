'''
Q7. how does input() function always return a string?
how can you convert it to another data type?

when user gives input keyboard sends sequence o char to python
'''

print("Enter number: ")
no1 = input()
print("display first number: ",type(no1))

# takes as a string eg. 24 will take as '2' and '4'

print("Enter another number: ")
no2 = float(input())
print("display anotehr number: ",type(no2))

value = bool(input("Enter something: "))

print(value)