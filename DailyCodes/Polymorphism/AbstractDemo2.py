from abc import ABC, abstractmethod
#abstract base class
#abstract -- without body
#concrete -- with body

class Base(ABC):
    @abstractmethod
    def addition(self,no1,no2):
        pass

class Derived(Base):
    def addition(self,no1,no2):
        return no1 + no2

dobj = Derived() 
Ret = dobj.addition(10,11)
print("Addition is : ",Ret)
