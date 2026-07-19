no = 11     #global variable

def Display():
    a = 21   #local variable
    print("from display value of a is: ",a)
    print("from display: ",no)

def Demo():
    print("from demo: ",no)
    print("from demo value of a is: ",a)  #error


Display()
Demo()