import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    # Step 1 : Load the data
    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values")
    print(df.head())

    print("Missing values : ")
    print(df.isnull().sum())  

    # Step 2 : Feature selection
    X = df[["AnnualIncome", "SpendingScore"]]

    print("Selected fetures : ")
    print(X.head())
    
if __name__ == "__main__":
    main()