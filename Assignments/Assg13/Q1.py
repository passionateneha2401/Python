'''
Write a program which accpets length and width of rectangle and prints area.
'''

def AreaRectangle(length,width):
    return (length*width)

def main():
    Length = float(input("Enter length of rectangle: "))
    Width  = float(input("Enter Width of rectangle: "))

    ret = AreaRectangle(Length,Width)
    print("Area of Reactangle is: ",ret)

if __name__ == "__main__":
    main()