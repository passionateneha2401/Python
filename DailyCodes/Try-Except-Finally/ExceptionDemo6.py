def main():

    ans = 0

    try: 
        print("Enter first number : ")
        no1 = int(input())

        print("Enter second number : ")
        no2 = int(input())

        ans = no1 / no2
        print("division is succesful")


    except ZeroDivisionError as zobj:
        print("exception occured due to second operand is zero : ",zobj)


    except ValueError as vobj:
        print("Exception occured due to invalid daya type : ",vobj)

    except Exception as eobj:
        print("Exception occured : ",eobj)

    finally:
        print("Inside finally block.")
     
    print("Result is : ",ans)
    
if __name__ == "__main__":
    main()