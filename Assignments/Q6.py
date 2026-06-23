import sys

print("Enter a value: ")
a = input()

print("Data type of a variable is: ",type(a))
print("Memory Address of a variable is: ",id(a))
print("Size of a variable is: ",sys.getsizeof(a),"bytes")

