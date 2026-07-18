def main():

    ans = 0

    try: 
        print("Enter first number : ")
        no1 = int(input())

        print("Enter second number : ")
        no2 = int(input())

        ans = no1 / no2
        print("division is succesful")
    
    except Exception as eobj:
        print("Exception occured : ",eobj)

     
    print("Result is : ",ans)
    
if __name__ == "__main__":
    main()