import os
def main():

    for FolderName,SubFolderName,FileName in os.walk("Marvellous"):
        print("Folder Name: ",FolderName)

        for subf in SubFolderName:
            print("SubFolder name : ",subf)
if __name__ == "__main__":
    main()