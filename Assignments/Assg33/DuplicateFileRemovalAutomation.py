#############################################################################
#
#   Import Required Libraries
#
#############################################################################

import os
import schedule
import time
import sys
import hashlib
import smtplib
from email.message import EmailMessage

#############################################################################
#
#   Function Name : SendMail
#   Input         : Log File Name
#   Description   : Sends log file through email
#   Date          : 23/07/2026
#   Author        : Neha Vilas Kumbhar
#
#############################################################################

def SendMail(LogFileName, StartTime, EndTime, DirectoryName, TotalFiles, DuplicateFound, DuplicateDeleted, ReceiverMail):

    try:
        msg = EmailMessage()

        msg["Subject"] = "Duplicate File Removal Log"
        msg["From"] = "demon10feb@gmail.com"
        msg["To"] = ReceiverMail

        Body = f"""
        Jay Ganesh,

        The duplicate-file removal operation has been completed successfully.

        Operation Statistics:

        Starting time of scanning : {StartTime}
        Completion time of scanning : {EndTime}
        Directory scanned : {DirectoryName}
        Total number of files scanned : {TotalFiles}
        Total number of duplicate files found : {DuplicateFound}
        Total number of duplicate files deleted : {DuplicateDeleted}

        Please find the detailed log file attached to this email.

        Regards,
        Neha Kumbhar🩷😎
        """

        msg.set_content(Body)

        with open(LogFileName, "rb") as f:
            FileData = f.read()

        msg.add_attachment(FileData,
                           maintype="application",
                           subtype="octet-stream",
                           filename=LogFileName)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login("demon10feb@gmail.com", "pvsbvsizjroxrpfy")

        server.send_message(msg)

        server.quit()

        print("Email sent successfully.")

    except Exception as e:
        print("Unable to send email :", e)

#############################################################################
#
#   Function Name : CalculateCheckSum
#   Input         : File Name
#   Output        : MD5 Checksum
#   Description   : Calculates checksum of a file
#   Date          : 23/07/2026
#   Author        : Neha Vilas Kumbhar
#
#############################################################################

def FindDuplicate(DirectoryName, ReceiverMail):
    Border = "-"*80

    timestamp = time.ctime()
    StartTime = time.ctime()

    LogFileName = "Marvellous %s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    ret = False

    ret = os.path.exists(DirectoryName)

    if(ret == False):
        print("Marvellous Automation Error : There is no such Directory with name ",DirectoryName)
        return  
    
    ret = os.path.isdir(DirectoryName)

    if(ret == False):
        print("Marvellous AUtomation Error : It is not a directory with name ",DirectoryName)
        return
    
    # Check directory access permission
    ret = os.access(DirectoryName, os.R_OK)

    if(ret == False):
        print("Marvellous Automation Error : Permission denied to access directory")
        return
        
    print("Log File gets created with name: ",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write(" Log files created: \n")
    fobj.write(Border+"\n")

    fobj.write("Starting Time : "+StartTime+"\n")
    fobj.write("Directory Scanned : "+DirectoryName+"\n")
    fobj.write(Border+"\n")

    Duplicate = {}
    TotalFiles = 0
    DuplicateDeleted = 0
    DuplicateFound = 0

    for FolderName, SubFolder, FileNames in os.walk(DirectoryName):

        for fname in FileNames:

            TotalFiles = TotalFiles + 1

            FilePath = os.path.join(FolderName, fname)

            filename = open(FilePath, "rb")

            hobj = hashlib.md5()

            Buffer = filename.read(1024)

            while(len(Buffer) > 0):
                hobj.update(Buffer)
                Buffer = filename.read(1024)

            filename.close()

            CheckSum = hobj.hexdigest()

            if(CheckSum in Duplicate):
                Duplicate[CheckSum].append(FilePath)
            else:
                Duplicate[CheckSum] = [FilePath]

    Flag = False

    print("\nDuplicate Files:\n")

    for Files in Duplicate.values():

        if(len(Files) > 1):
            DuplicateFound = DuplicateFound + (len(Files) - 1)
            Flag = True

            for File in Files:
                print(File)

            # Delete duplicate files except the first one
            for File in Files[1:]:
                if os.access(File, os.W_OK):
                    if(os.path.isfile(File)):
                        try:
                            os.remove(File)
                        except Exception as e:
                            fobj.write(str(e)+"\n")
                else:
                    fobj.write("Permission denied : " + File + "\n")

                fobj.write("Deleted : "+File+"\n")
                DuplicateDeleted = DuplicateDeleted + 1
                fobj.write(File + " Deleted\n")
                fobj.write("Checksum : "+CheckSum+"\n")

            print(Border)

    if(Flag == False):
        print("No duplicate files found.")

    
    EndTime = time.ctime()
    fobj.write("Completion Time : "+EndTime+"\n")

    fobj.write(Border+"\n")

    fobj.write(f"Total files scanned : {TotalFiles}\n")
    fobj.write(f"Total duplicate files found : {DuplicateFound}\n")

    fobj.write(f"Total duplicate files deleted : {DuplicateDeleted}\n")
    fobj.write("Errors Encountered : None\n")
    fobj.write("Email Delivery Status : Pending\n")

    fobj.write(Border+"\n")

    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()
    SendMail(
        LogFileName,
        StartTime,
        EndTime,
        DirectoryName,
        TotalFiles,
        DuplicateFound,
        DuplicateDeleted,
        ReceiverMail
    )

#############################################################################
#
#   Function name :    main
#   Input :            command line arguments
#   Description :      it controls the script
#   Date :             23/07/2026
#   Author :           Neha Vilas Kumbhar
#
#############################################################################

def main():
    Border = "-"*80
    print(Border)
    print(" Marvellous Automation Script")
    print(Border)

 
    if(len(sys.argv) == 4):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please excute the script as ")
            print("Python FileName.py DirectoryName")
            print("Directory Name should be Absolute Path")
        else:
            if "@" not in sys.argv[3]:
                print("Invalid Email")
                return
            try:
                Interval = int(sys.argv[2])

                if Interval <= 0:
                    print("Invalid Time Interval")
                    return

            except ValueError:
                print("Time Interval should be integer")
                return
            schedule.every(Interval).minutes.do(FindDuplicate,sys.argv[1],sys.argv[3])
 

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