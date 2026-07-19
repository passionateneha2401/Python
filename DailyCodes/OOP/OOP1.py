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
        print(self.value1)
        print(self.value2)

dobj = Demo()
dobj.fun()