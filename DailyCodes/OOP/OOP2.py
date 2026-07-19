class Demo:
    #class variables
    value1 = 10
    value2 = 20

    #instance var
    def __init__(self):
        self.no1 = 11
        self.no2 = 21

    #instance method
    def fun(self):
        print("Inside instance method named as fun")
        print(self.no1)
        print(self.no2)
        print(Demo.value1)
        print(Demo.value2)   #to access class var two ways are there self. & classname.---use classname.---hdfc.roi is better

#object creation
dobj = Demo()
dobj.fun()