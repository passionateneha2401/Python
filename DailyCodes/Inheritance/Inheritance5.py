class Base:
    def fun(self):
        print("Inside Base fun")

class Derived(Base):         
    def sun(self):
        print("inside derived sun")

dobj = Derived()

dobj.fun()
dobj.sun()
