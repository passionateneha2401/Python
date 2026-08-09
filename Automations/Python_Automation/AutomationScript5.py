import sys

def main():
    print("--------------------------------------------------------------------")
    print(" Marvellous Automation Script")
    print("--------------------------------------------------------------------")
 
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please excute the script as ")
            print("Python FileName.py DirectoryName")
            print("Directory Name should be Absolute Path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name : ",DirectoryName)
    else:
        print("Invalid number of argumengts")
        print("Please use --h or --u for more informattion.")
    
    print("-------------------------------------------------------------------")
    print(" Thank you for using Marvellous Automation Script")
    print("-------------------------------------------------------------------")

if __name__ == "__main__":
    main()
