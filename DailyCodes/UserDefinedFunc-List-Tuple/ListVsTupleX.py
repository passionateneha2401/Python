#---------------------------------------------
#            list    tuple
#----------------------------------------------
# ordered    yes      yes
# indexed    yes      yes
# mutable    yes      no
# hetero     yes      yes
#-----------------------------------------------

def main():
    data1 = [10,3.14,True,"Pune"]    #list----heterogenous
    data2 = (10,3.14,True,"Pune")    #tuple

    print(data1)
    print(data2)

    print(data1[0])
    print(data2[0])

if __name__ == "__main__":
    main()

#if a data is indexed then it is ordred and vice versa
#the language which is dynamically ttypes can never be homogenous
#everything is hetero in python except string!!!!
#array is homo but here in program its hetero