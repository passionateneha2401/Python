print("---------------------------------------")
print("--------Ticket Pricing Software--------")
print("---------------------------------------")

print("Enter your age : ")
Age = int(input())

if(Age<0 and Age>=5):
    print("Free Entry")
elif(Age>5 and Age<=18):
    print("Pay 900")
elif(Age>18 and Age<=40):
    print("Pay 1200")
else:
    print("Pay 500")