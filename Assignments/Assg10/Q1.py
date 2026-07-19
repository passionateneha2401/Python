'''
Write a program which accepts one number and prints multiplication table of that number.
Input: 4
Output: 4 8 12 16 20 24 28 32 36 40

'''
def MultiplicationTable(no):
    for i in range(1,11):
        print(no * i)
        #print(f"{no} x {i} = {no * i})
def main():
    value = int(input("Enter a number: "))
    MultiplicationTable(value)

if __name__ == "__main__":
    main()