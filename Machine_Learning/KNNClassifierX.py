import numpy as np
from sklearn.neighbors import KNeighborsClassifier
# import pandas as pd


def main():
    # Independent
    # X = pd.Dataframe('use dataframe instaed of array)
    X = np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]
    ])

    # Dependent
    Y = np.array(["Red","Red","Blue","Blue"])

    new_point = np.array([[3,3]])

    print("Independet variables are : ")
    print(X)

    print("Dependet variables are : ")
    print(Y)

    print("testing point is  :")
    print(new_point)

if __name__ == "__main__":
    main()