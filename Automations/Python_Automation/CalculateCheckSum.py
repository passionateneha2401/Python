import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1000)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()



def main():
    ret = CalculateCheckSum("demo.txt")
    print("Checksum of file is : ",ret)

if __name__ == "__main__":
    main()