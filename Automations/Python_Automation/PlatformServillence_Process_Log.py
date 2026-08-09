import psutil
import sys 
import os
import time
import schedule
def ProcessScan():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        print("-------------------------------------------------------")
        print(info)
        print("-------------------------------------------------------")


def PlatformServillance(FolderName):
    border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret =os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as folder name is existing but its not a directory.")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log File gets succesfully created with name {FileName}")

    fobj.write(border+"\n")
    fobj.write("----Marvellous Platform Servillence System----\n")
    fobj.write(f"Log File gets created at : {timestamp}"+"\n")
    fobj.write(border+"\n\n")
    fobj.write("----------System Report------------\n")

    #CPU Information
    fobj.write("Number of active cpu cores : %s \n"%psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n"%psutil.cpu_percent())
    fobj.write(border+"\n")

    #RAM Information
    memory = psutil.virtual_memory()

    fobj.write("RAM Usage : %s %%\n"%memory.percent)
    fobj.write("Total RAM avl : %s\n"%memory.total)
    fobj.write(border+"\n")

    #Network usage
    netobj = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n"%(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n"%(netobj.bytes_recv / (1024 * 1024)))

    fobj.write(border+"\n")




    fobj.write("\n\n\n\n\n\n\n\n\n\n")

    fobj.write(border+"\n")
    fobj.write("----------------End of log file------------------\n")
    fobj.write(border+"\n")

    fobj.close()

def main():
    ProcessScan()
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

     #   print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduler started succesfully")
        print("Press ctrl + c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformServillance,sys.argv[2])
                
        while True:
            schedule.run_pending()
            time.sleep(1)


    else :
        print("Invalid Number of Arguments")
        print("Unable to proceed as args are not matching")
        print("Please use --h or --u for more details")


    print(border)
    print(" Thank you for using Marvellous Platform Servillence System ")
    print(border)

if __name__ == "__main__":
    main()