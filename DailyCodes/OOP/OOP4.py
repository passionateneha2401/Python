class Demo:
    #class variables
    value1 = 10
    value2 = 20

    #class var
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
    
    @classmethod
    def gun(cls):
        print("Inside instance method named as gun")
        print(Demo.value1)
        print(Demo.value2)
         
#call with object
dobj = Demo()
dobj.gun()     #there is no instance of class