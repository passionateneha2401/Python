'''
Design a Python application that creates three threads named Small,Capital and Digits.
- Both threads should accpet a string as input.
- A Small thread should count and display the number of lowercase characters.
- A Capital thread should count and display the number of uppercase characters.
- A Digits thread should count and display the number of  numeric digits.
- Each thread should display :
          • Thread ID
          • thread Name
'''
import threading

def Small(value):
    print("Name of the thread is : ",threading.current_thread().name)
    print("ID of the thread is : ",threading.get_ident())
    SmallCount = 0
    for ch in value:
        if(ch >= 'a' and ch <= 'z'):    
            print(ch , end = " ")
            SmallCount = SmallCount + 1
    print( )
    print("lowercase letters in the string are : ",SmallCount)
    

def Capital(value):
    print("Name of the thread is : ",threading.current_thread().name)
    print("ID of the thread is : ",threading.get_ident())

    CapitalCount = 0
    for ch in value:
        if(ch >= 'A' and ch <= 'Z'):
            print(ch , end = " ")
            CapitalCount = CapitalCount + 1
    print( )
    print("uppercase letters in the string are : ",CapitalCount)

def Digits(value):
    print("Name of the thread is : ",threading.current_thread().name)
    print("ID of the thread is : ",threading.get_ident())

    DigitsCount = 0
    for ch in value:
        if(ch >= '0' and ch<= '9'):
            print(ch, end = " ")
            DigitsCount = DigitsCount + 1
    print( )
    print("Digits in the string are : ",DigitsCount)




def main():
    val = input("Enter string: ")


    t1 = threading.Thread(target = Small,args= (val, ),name = "Small")
    t2 = threading.Thread(target = Capital,args = (val, ),name = "Capital")
    t3 = threading.Thread(target = Digits, args = (val,), name = "Digits" )

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

if __name__ == "__main__":
    main()

        