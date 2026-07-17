'''
1.Write a Python program to implement a class named Demo with following specifications : 
The class should contain two instance var : no1 and no2.
The class should contain one class variable named Value.
Define contructor (__init__) that accepts two para and initiales instance var.
Implement two instance methods : 
      Fun() - Displays the values of ins var no1 & no2.
      Gun() - Displays the values of ins var no1 & no2.

Create two objects of Demo class as follows : 
obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)
Call inst methods in given sequence : 

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
'''

class Demo:
    value = 28

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Inside instance method Fun : ")
        print("value of no1 : ",self.no1)
        print("Value of no2 : ",self.no2)
    
    def Gun(self):
        print("Inside instance method Gun : ")
        print("value of no1 : ",self.no1)
        print("Value of no2 : ",self.no2)

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
