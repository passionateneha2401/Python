'''
Write a program which accpets one number and prints that many numbers starting from one.
Input: 5
Ouput: 1 2 3 4 5

'''

def FromStart(no):
    values = []
     
    for i in range(1,no+1):
          values.append(i)
    
    return values
          

def main():
    ret = FromStart(5)
    print("Numbers from 1 upto number itself: ",*ret)

if __name__ == "__main__":
    main()