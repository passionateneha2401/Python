import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-"*80

    # Step 1 : Load the dataset
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("some entrues from dataset : ")
    print(df.head())
    print(border)

    # Step 2 : Clean the dataset
    print(border)
    print("Step 2 : Clean the dataset from CSV file")
    print(border)

    df.dropna(inplace=True)

    print("Shape of dataset : ",df.shape)
    print("Total Records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    # Step 3 : Seperte independet and dependetn variables

    print(border)
    print("Step 3 : Seperte independet and dependetn variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']


    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input Columns : ",X.columns.tolist())
    print("Ouput columns : Class")
    print(border)

    # Step 4 : Split the dataset in training and testing
    
    print(border)
    print("Step 4 : Seperte independet and dependetn variables")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("deatils of tranong and testing data")

    print("shape of X_train:",X_train.shape)
    print("shape of X_test:",X_test.shape)
    print("shape of Y_train:",Y_train.shape)
    print("shape of Y_test:",Y_test.shape)

    print(border)

    # Step 5 : Feature Scaling
    
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("feature scaling done")

    print(border)

    # Step 6 :Hyperparamter tuning

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors =k)
        model = model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)

        accuracy_scores.append(accuracy)

    print("Accuracy report : ")

    for no in accuracy_scores:
        print(no)

    print(border)

    print(border)
    print("graphical representation")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker="o")

    plt.title("k values vs accuracy")
    plt.xlabel("Values of k")
    plt.ylabel("Accuracy")
    plt.grid(True)

    plt.xticks(list(K_values))

    plt.show()




def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()