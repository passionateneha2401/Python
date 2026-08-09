import os
def main():

    for FolderName,SubFolderName,FileName in os.walk("Marvellous"):

        for fname in FileName:
            print("file name : ",fname)
if __name__ == "__main__":
    main()