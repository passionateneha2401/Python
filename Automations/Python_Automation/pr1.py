import os

try:
    fobj = open("demo.txt","r")

except FileNotFoundError as fnf:
    print("File not found")

