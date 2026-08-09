# python Automation.py --h
import sys

def main():
 
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("Help")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage")
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name : ",DirectoryName)
    else:
        print("Invalid number of argumengts")
        print("Please use --h or --u for more informattion.")

if __name__ == "__main__":
    main()