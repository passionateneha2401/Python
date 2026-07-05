'''
Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.
'''
CheckLength = lambda value : (len(value))>5

def main():
    values = int(input("Enter how many strings u want to enter: "))
    StringList = []

    for i in range(values):
        StringInput = input("Enter string: ")
        StringList.append(StringInput)
    print("List of strings is: ",StringList)

    Fdata = list(filter(CheckLength,StringList))
    print("Strings of length 5 are: ",Fdata)
if __name__ == "__main__":
    main()