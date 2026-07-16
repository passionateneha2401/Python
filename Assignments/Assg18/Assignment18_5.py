'''
Write a program whcich accept N number from user and store it into List.
return addition of all prime numbers from that List. Main python file accpets 
N numbers from user and pass each number to ChkPrime() function which is part of our user
defined module named MarvellousNum. Name of fucntion from main python file should be ListPrime().
Input : Number of elemnts : 11
Input elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 + 2 + 5) 
'''
import MarvellousNum 

def Addition(elmts):
    
    total = 0
    for value in elmts:
        if MarvellousNum.ChkPrime(value):
            total = total + value
    return total



def main():
    values = int(input("Number of elements : "))
    no = []

    for i in range(values):
        num = int(input("Enter number: "))
        no.append(num)
    print("List is : ",no)

    ret = Addition(no)
    print("Addition of prime numbers in list is: ",ret)

if __name__ == "__main__":
    main()