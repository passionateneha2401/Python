class Base:
    def __init__(self):
        print("Inside Base Constructor")

class Derived(Base):         
    def __init__(self):
        print("Inside Derived Constrctor")

bobj = Base()
