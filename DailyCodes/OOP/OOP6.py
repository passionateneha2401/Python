class Demo:
    #class variables
    value1 = 10
    value2 = 20
    #classname.

    #instance var
    def __init__(self):
        self.no1 = 11
        self.no2 = 21
        #instnace.

obj1 = Demo()
obj2 = Demo()

obj1.no1 = 0

print(obj1.no1)       #0
print(obj2.no1)       #11

#obj1.value1 = 0 
#classname.var
Demo.value1 = 0
#print(obj1.value1)
#print(obj2.value1)

print(Demo.value1)