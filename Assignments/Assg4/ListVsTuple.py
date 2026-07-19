#---------------------------------------------
#            list    tuple
#----------------------------------------------
# ordered    yes      yes
# indexed    yes      yes
# mutable    yes      no
#-----------------------------------------------

def main():
    data1 = [10,20,30,40]    #list
    data2 = (10,20,30,40)    #tuple

    print(data1)
    print(data2)

    print(data1[0])
    print(data2[0])

if __name__ == "__main__":
    main()

#if a data is indexed then it is ordred and vice versa