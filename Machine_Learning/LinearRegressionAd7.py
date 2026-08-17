import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(datapath):
    border = "-" * 40


    # Step 1 : Load the data
    print(border)
    print("Step 1 : ")
    print(border)

    df = pd.read_csv(datapath)

    print(df.head())

    # Step 2 : Remove unwanted columns
    print(border)
    print("# Step 2 : Remove unwanted columns ")
    print(border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    # Step 3 : Check Missing Values
    print(border)
    print("## Step 3 : Check Missing Values")
    print(border)

    print("Total missing values : ")
    print(border)
    print(df.isnull().sum())
    print(border)

    # Step 4 : Statstitical summary
    print(border)
    print("# Step 4 : Statstitical summary")
    print(border)

    print(df.describe())

    # Step 5 : Correlation
    print(border)
    print("# Step 5 :Correlation")
    print(border)

    print(df.corr())

    # Step 6 : Seperate indepdent and dependent variables
    print(border)
    print("#Step 6 : Seperate indepdent and dependent variables")
    print(border)

    X = df[["TV", "radio", "newspaper"]]
    Y = df["sales"]

    print("Indepodent variables: ")

    print(X.head())

    print("Depodent variables: ")

    print(Y.head())

    # Step 6 : Split indepdent and dependent variables
    print(border)
    print("#Step 6 : Split indepdent and dependent variables")
    print(border)

    X_train, X_test, Y_train, Y_test =  train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data : ",X_train.shape)
    print("Testing Data : ",Y_train.shape)

    # Step 8 : Create & train model
    print(border)
    print(" # Step 8 : Create & train model")
    print(border)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    print("model trained successfully")


    # Step 9 : test the model
    print(border)
    print(" # Step 9 : test model")
    print(border)

    y_pred = model.predict(X_test)

    print("Expected answer: ")
    print(Y_test[:3])

    print("Predicted answer: ")
    print(y_pred[:3])




def main():
    MarvellousRegression("Advertising.csv")
    
if __name__ == "__main__":
    main()
