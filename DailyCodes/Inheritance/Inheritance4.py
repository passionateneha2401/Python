class Base:
    def fun(self):
        print("Inside Base fun")

class Derived(Base):         
    pass

dobj = Derived()
dobj.fun()
