'''
Write a program which accpets one number and prints all even numbers till that number.
Input: 10
Ouput: 2 4 6 8 10

'''
def EvenNumbers(no):
    for i in range(no+1):
        if(i % 2 == 0):
            print(i)

def main():
    EvenNumbers(10)

if __name__ == "__main__":
    main()