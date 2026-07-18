from abc import ABC, abstractmethod
#abstract base class
#abstract -- without body
# concrete -- with body

class Base(ABC):
    @abstractmethod
    def addition(self,no1,no2):
        pass

class Derived(Base):
    pass

dobj = Derived()        #Error
