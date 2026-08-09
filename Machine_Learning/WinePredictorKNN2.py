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


    

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()