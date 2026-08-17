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

#step 3 : splitting
#----------------------------------------------------------------------
#  Function Name : SplitData
#  Description : it performs splitting activity
#  Input : dataframe
#  Output : 4 subset for traning and testing
#  Authot : Neha Vilas Kummbhar
#  Date : 16/08/2026
#------------------------------------------------------------------------

def SplitData(df):
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        test_size=0.2
    )

    print("dataset splitting complted succeefully")
    return X_train, X_test, Y_train, Y_test

#step 3 : train model
#----------------------------------------------------------------------
#  Function Name : TrainModel
#  Description : it performs model training
#  Input : traning features and labels
#  Output : trained model
#  Authot : Neha Vilas Kummbhar
#  Date : 16/08/2026
#------------------------------------------------------------------------

def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train, Y_train)

    print("model trianed successfully")

    return model

#step 5 : evaluate model
#----------------------------------------------------------------------
#  Function Name : EvaluateModel
#  Description : it performs model testing
#  Input : model, testing data(features, labels)
#  Output : none
#  Authot : Neha Vilas Kummbhar
#  Date : 16/08/2026
#------------------------------------------------------------------------
def EvaluateModel(model, X_test,Y_test):
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test,Y_pred)

    print("accuracy",accuracy)

    print(confusion_matrix(Y_test,Y_pred))
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

    # step 3
    X_train, X_test, Y_train, Y_test = SplitData(df) 

    # step 4
    model = TrainModel(X_train, Y_train)

    # step 5
    EvaluateModel(model,X_test , Y_test)

if __name__ == "__main__":
    main()