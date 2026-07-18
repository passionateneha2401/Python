'''
Write a program which display first 10 even numbers on screen.
2 4 6 8 10 12 14 16 18 20
'''

def DisplayEven():
    for i in range(2,21,2):
        print(i, end=" ")


def main():
    DisplayEven()

if __name__ == "__main__":
    main()


