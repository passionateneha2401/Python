import numpy as np
import math

def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X']-P2['X'])**2 + (P1['Y']-P2['Y'])**2)
    return Ans


# procedural
def MarvellousKNNClassifier():
    border = "-"*50

    data = [
        {'point':'A', 'X' : 1, 'Y':2, 'label':'Red'},
        {'point':'B', 'X' : 2, 'Y':3, 'label':'Red'},
        {'point':'C', 'X' : 3, 'Y':1, 'label':'Blue'},
        {'point':'D', 'X' : 5, 'Y':6, 'label':'Blue'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for i in data:
        print(i)

    print(border)

    new_point = {'X':3,'Y':3}

    result = MarvellousEucDistance(data[0],new_point)

    print("distance is : ",result)


def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()