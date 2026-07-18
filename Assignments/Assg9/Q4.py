'''

Write a progtam which accpets one nuber and pritns cube of that number

'''
def CubeOfNumber(no):
    cube = (no)** 3      #exponenet operator
    #cube = pow(no, 3)
    return cube

def main():
    value = int(input("Enter a Number: "))
    ret = CubeOfNumber(value)
    print("Cube of number is: ",ret)

if __name__ == "__main__":
    main()