# procedural
def MarvellousKNNClassifier():
    border = "-"*30

    data = [
        {'point':'A', 'X' : 1, 'Y':2, 'label':'Red'},
        {'point':'B', 'X' : 2, 'Y':3, 'label':'Red'},
        {'point':'C', 'X' : 3, 'Y':1, 'label':'Blue'},
        {'point':'D', 'X' : 5, 'Y':6, 'label':'Blue'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    print(data)

    print(border)


def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()