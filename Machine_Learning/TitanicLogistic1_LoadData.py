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

#----------------------------------------------------------------------
#  Function Name : main
#  Description : entry point function
#  Input : none
#  Output : none
#  Authot : Neha Vilas Kummbhar
#  Date : 16/08/2026
#------------------------------------------------------------------------
def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()