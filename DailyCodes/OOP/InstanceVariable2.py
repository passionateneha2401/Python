class Marvellous:
    #class variable
    No1 = 11
    No2 = 12

    def __init__(self):
        #instance variable
        self.Value1 = 21
        self.Value2 = 51

print(Marvellous.No1)
print(Marvellous.No2)

#object/instance creatiion

mobj1 = Marvellous()
mobj2 = Marvellous()
mobj3 = Marvellous()

print(mobj1.Value1)
print(mobj2.Value2)


#inside init --> instance variable
#outside init --> class variable/statuc variable in c++ or java
# class var shared to all objects of class!
# swatachya plate madhla basundi--> swatachya.basundi(self.basundi-->self.value)

#init method is complusion to wrte to  make instace variable! w/o init no instance

#inst var is a part of object...class var is a part of class