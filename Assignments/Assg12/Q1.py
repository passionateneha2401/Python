'''
Write a program which accepts one character and checks whther it is vowel or consonanat.
Input: a
Output: Vowel

'''

def ChecksVowel(val):
    value = ['a','e','i','o','u']

    if val in value:
        return True
    else:
        return False

def main():
    ret = ChecksVowel('a')
    
    if(ret == True):
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()