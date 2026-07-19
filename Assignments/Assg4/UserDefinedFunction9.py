def BigBazar():
    print("Inside Big Bazaar..")

    def Amul():
        print("inside amul ice cream parlour..")
    #if u want to call amul() u have to call first run bigbazar
    # we cant call samul through main
    Amul()

def main():
    BigBazar()   #allowed

    

    
if __name__ == "__main__":
    main()