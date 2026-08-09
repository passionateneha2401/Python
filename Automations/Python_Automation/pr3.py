import os

def display(filename):
    fobj = open(filename,"r")

    lines = fobj.readlines()
    line_count = len(lines)

    word_count = 0

    for line in lines:
        word_split = line.split()
        word_count = word_count + len(word_split)

    print("line count : ",line_count)
    print("word count : ",word_count)

    fobj.close()


def main():
    test_file = open("demo.txt","w")
    test_file.write("Marvellous Infosystems...")
    test_file.close()

    display("demo.txt")

if __name__ == "__main__":
    main()