import sys
import os

def DirectoryScanner(DirectoryPath):

    print("Files from the directory are : ")

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):

        for fname in FileName:
            print(fname)


def main():
    Border = "-"*80
    print(Border)
    print(" Marvellous Automation Script")
    print(Border)

 
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please excute the script as ")
            print("Python FileName.py DirectoryName")
            print("Directory Name should be Absolute Path")
        else:
            
            DirectoryScanner(sys.argv[1])
    else:
        print("")
    
    print(Border)
    print(" Thank you for using Marvellous Automation Script")
    print(Border)
if __name__ == "__main__":
    main()
