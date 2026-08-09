import pandas as pd

def main():
    Data = {
        "Name" : ["Sagar","Amit","Pooja"],
        "Age" : [27,28,25],
        "City" : ["Pune","Kolhapur","Satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj)

    #print(dobj[0]) Not Allowed

    print(dobj["Age"])    

if __name__ == "__main__":
    main()