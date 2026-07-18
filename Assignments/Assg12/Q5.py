'''
Write a program which accpets one number AND PRINTS THAT MANY NUMBERS IN REVERSE ORDER.
Input: 5
Ouput: 5 4 3 2 1

'''

def ReverseOrder(no):

    values = []
    for i in range(no,0,-1):
        values.append(i)
    return values
    

def main():
    ret = ReverseOrder(5)
    print("Numbers in reverse order: ",*ret)

if __name__ == "__main__":
    main()