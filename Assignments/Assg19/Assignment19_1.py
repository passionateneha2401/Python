'''
Write a program which conatins one lambda function which accepts one 
parameter and return power of two.
Input : 4        Output : 16
Input : 6        Output : 64
'''

Answer = lambda a : a ** 2

def main():
    value = int(input("Enter number : "))

    ret = Answer(value)
    print(f"Power of two of {value} is : {ret}")

if __name__ == "__main__":
    main()