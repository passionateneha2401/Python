class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside descturctor") #before deallocating memory...at end memory will go!

obj1 = Demo()
obj2 = Demo()

print("End of application.")