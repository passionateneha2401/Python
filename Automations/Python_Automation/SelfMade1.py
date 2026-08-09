#############################################################################
#
#   Importing Required Libraries
#
##############################################################################
import sys
import os
import time
import schedule

#############################################################################
#
#   Function name :    DirectoryScanner
#   Input :            Name of Directory
#   Description :      Deletes all empty files periodically
#   Date :             19/07/2027
#   Author :           Neha Vilas Kumbhar
#
#############################################################################

def DirectoryScanner(DirectoryPath):
    Border = "-"*80

    timestamp = time.ctime()

    LogFileName = "Marvellous %s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    ret = False

    ret = os.path.exists(DirectoryPath)

    if(ret == False):
        print("Marvellous Automation Error : There is no such Directory with name ",DirectoryPath)
        return  
    
    ret = os.path.isdir(DirectoryPath)

    if(ret == False):
        print("Marvellous AUtomation Error : It is not a directory with name ",DirectoryPath)
        return
    
    print("Log File gets created with name: ",LogFileName)
    
    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write(" Log files created: \n")
    fobj.write(Border+"\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles = TotalFiles + 1
            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname}:  {os.path.getsize(fname)}bytes\n")

            if(os.path.getsize(fname) == 0):
                EmptyFiles = EmptyFiles + 1
                os.remove(fname)

    fobj.write(Border+"\n")

    fobj.write(f"Total files scanned : {TotalFiles}\n")
    fobj.write(f"Total empty files found and deleted : {EmptyFiles}\n")

    fobj.write(Border+"\n")

    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")
    fobj.close()

#############################################################################
#
#   Function name :    main
#   Input :            command line arguments
#   Description :      it controls the script
#   Date :             19/07/2027
#   Author :           Neha Vilas Kumbhar
#
#############################################################################

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
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
 

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("")
    
    print(Border)
    print(" Thank you for using Marvellous Automation Script")
    print(Border)

#############################################################################
#
#   Starter of the Automation Script
#
#############################################################################
if __name__ == "__main__":
    main()
