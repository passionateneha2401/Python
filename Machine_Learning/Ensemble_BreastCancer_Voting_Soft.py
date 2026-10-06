import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score , confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

#---------------------------------------
# Step 1 : Load the dataset
#---------------------------------------

df = pd.read_csv("breast_cancer.csv")

print("Shape of dataset : ", df.shape)

print("First few records : ")
print(df.head())

#---------------------------------------
# Step 2 : Separate fetures and labels
#---------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

#---------------------------------------
# Step 3 : Split dataset for traiing and testing
#---------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
                                            X,
                                            Y,
                                            test_size=0.2,
                                            random_state=42
                                            )

#---------------------------------------
# Step 4 : Scale the fetures
#---------------------------------------

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

#---------------------------------------
# Step 5.1 : Create the Individual models
#---------------------------------------

model_log = LogisticRegression(max_iter=1000)

model_det = DecisionTreeClassifier(random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)

#---------------------------------------
# Step 5.2 : Create the Voting models
#---------------------------------------

model = VotingClassifier(
    estimators=[
        ('logistic',model_log),
        ('decision_tree',model_det),
        ('knn',model_knn)
    ],
    voting='soft'
)

#---------------------------------------
# Step 6 : Train the model
#---------------------------------------

model = model.fit(X_train,Y_train)

#---------------------------------------
# Step 7 : Test the model
#---------------------------------------

Y_pred = model.predict(X_test)

#---------------------------------------
# Step 8 : Evalaute the mdoel
#---------------------------------------

print("Accuracy : ",accuracy_score(Y_test,Y_pred))

print("Confustion matrix : ")
print(confusion_matrix(Y_test,Y_pred))