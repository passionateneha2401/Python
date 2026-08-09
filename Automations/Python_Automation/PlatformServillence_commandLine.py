#python ProcessServillence.py 2 MarvellousLog
#python ProcessServillence.py time_interval Folder_Name
#           0                     1            2
# len(sys.argv) -> 3

#python proceeserv.py --h
#python proceeserv.py --u
#                 0     1 
# len(sys.argv) -> 2



import psutil
import sys 
import os

def main():
    border = "-"*50
    print(border)
    print("----Marvellous Platform Servillence System----")
    print(border)

    # --h and --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform : ")
            print("1 : It fetch the info of running processes")
            print("2 : It fetch info about the primary storage as RAM")
            print("3 : It fetch info about the secondary storage as HDD")
            print("4 : It fetch info about the Microprocessor")
            print("5 : It fetch info about it gets autoshcedule periodically")
            print("6 : It maintians all records into log file")
            print("7 : It sends mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python3 {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in mins for periodic execution")
            print("Folder_Name : name of folder for log file creation")

        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details.")
  

    # --Actual project code
    elif(len(sys.argv) == 3):
        pass

    else :
        print("Invalid Number of Arguments")
        print("Unable to proceed as args are not matching")
        print("Please use --h or --u for more details")


    print(border)
    print(" Thank you for using Marvellous Platform Servillence System ")
    print(border)

if __name__ == "__main__":
    main()