def main():
    marks = [78,90,56,98,77]

    for no in marks:
        print(no)
        
    marks[2] = 59
    print("-"*15)

    for no in marks:
        print(no)
    
    

if __name__ == "__main__":
    main()