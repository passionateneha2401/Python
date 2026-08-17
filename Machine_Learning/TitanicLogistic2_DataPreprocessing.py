import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# step 1 : load data

#----------------------------------------------------------------------
#  Function Name : LoadData
#  Description : Load the data from csv
#  Input : Name of csv file
#  Output : Data Frame
#  Authot : Neha Vilas Kummbhar
#  Date : 16/08/2026
#------------------------------------------------------------------------
def LoadData(filename):
    df = pd.read_csv(filename)

    print("dataset loaded succeefully")
    print(df.head())

    return df

#step 2 : EDA
#----------------------------------------------------------------------
#  Function Name : PreprocessData
#  Description : it performs data analysis
#  Input : dataframe
#  Output : Updated Data Frame
#  Authot : Neha Vilas Kummbhar
#  Date : 16/08/2026
#------------------------------------------------------------------------
def PreprocessData(df):
    df = df.drop([
        "zero",
        "Passengerid",
        "name"
    ],
    errors = "ignore"
    )

    # Handle missing values 
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # convert categorical to numberic data
    df =pd.get_dummies(
        df,
        columns = ["Embarked"],
        drop_first=True,
        dtype=int
    )
    print(df.head())

    print("Data preprocessing has been completed!!")

    return df

#----------------------------------------------------------------------
#  Function Name : main
#  Description : entry point function
#  Input : none
#  Output : none
#  Authot : Neha Vilas Kummbhar
#  Date : 16/08/2026
#------------------------------------------------------------------------
def main():
    #step 1 
    df = LoadData("MarvellousTitanicDataset.csv")

    # step 2 
    df = PreprocessData(df)

if __name__ == "__main__":
    main()