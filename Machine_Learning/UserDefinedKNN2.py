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


def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()