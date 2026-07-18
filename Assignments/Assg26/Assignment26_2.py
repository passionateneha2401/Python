'''
1.Write a Python program to implement a class named Circle with following specifications : 
The class should contain 3 instance var : Radius,Area and Circumference.
The class should contain one class variable named PI,initialized to 3.14.
Define contructor (__init__) that initiales all instance var to 0.0.
Implement two instance methods : 
    Accept() - accepts the radius of the circle from the user.
    CalculateArea() - calculates the area of the circle and stores it in Area variable.
    CalculateCircumference() - calculates the circumference of the circle and store the Circusmference variable.
    Display() - displays the values Radius,Area and Circumference.

Create multiple objects of the Circle class and imvoke all instance methods for each object.
'''

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Inside the instance method")
        self.Radius = float(input("Enter radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
  
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)
  


obj = Circle()
obj.Accept()
obj.CalculateArea()
obj.CalculateCircumference()
obj.Display()
