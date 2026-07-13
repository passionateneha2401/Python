class Base1:
    def fun(self):
        print("Inside Base1 fun")

class Base2:
    def gun(self):
        print("Inside Base2 gun")

class Derived(Base1,Base2):         
    def sun(self):
        print("inside derived sun")

dobj = Derived()

dobj.fun()
dobj.gun()
dobj.sun()
