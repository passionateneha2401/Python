def BigBazar():
    print("Inside Big Bazaar..")

    def Amul():
        print("inside amul ice cream parlour..")

def main():
    BigBazar()   #allowed
    Amul()   #Error
    BigBazar.Amul()     #Error
    

    
if __name__ == "__main__":
    main()