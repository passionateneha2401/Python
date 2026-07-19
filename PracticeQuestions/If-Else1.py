'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


and  is even, so it is not weird.
'''

def myFunction(n):
    if n % 2 == 0 and n in range(2,7):
        print("Not Weird")
    elif (n % 2 == 0 and n in range (6,21)) or (n % 2 != 0):
        print("weird")
    elif(n % 2 == 0 and n > 20):
        print("not weird")
    else:
        print("weird")
    return n

def main():
    print("Enter a number: ")
    no = int(input())

    ret = myFunction(no)
    print("Result is: ",no)

if __name__ == "__main__":
    main()

