'''
Write a program which accpets radius of circle and prints area of circle.
'''

def AreaCircle(radius):
    return (3.142 * radius * radius)

def main():
    Radius = float(input("Enter Radius of circle: "))

    ret = AreaCircle(Radius)
    print("Area of circle is: ",ret)

if __name__ == "__main__":
    main()
