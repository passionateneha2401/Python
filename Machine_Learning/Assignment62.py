import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


#-----------------------------------------
# 1. Read the data from CSV
#-----------------------------------------

print("1. Read the data from CSV")

data = pd.read_csv("Employee_Attrition.csv")

print("Complete Dataset : ")
print(data)


#-----------------------------------------
# 2. Data Analysis (EDA)
#-----------------------------------------

print("2. Data Analysis")

print("First 5 rows : ")
print(data.head())

print("Columns : ")
print(data.columns)

print("Size of data : ")
print(data.shape)

print("Missing values : ")
print(data.isnull().sum())

print("Statistical Summary : ")
print(data.describe())


#-----------------------------------------
# 3. Preprocessing
#-----------------------------------------

print("3. Preprocessing")

# Separate input and target
X = data.drop("Attrition", axis=1)
Y = data["Attrition"]

print("Input features : ")
print(X.head())

print("Target : ")
print(Y.head())


# Convert OverTime Yes/No into 1/0
X['OverTime'] = X['OverTime'].map({'Yes': 1, 'No': 0})

# Convert Attrition Yes/No into 1/0
Y = Y.map({'Yes': 1, 'No': 0})

print("After converting OverTime : ")
print(X.head())

print("After converting Attrition : ")
print(Y.head())


#-----------------------------------------
# 4. Train Test Split
#-----------------------------------------

print("4. Train Test Split")

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("Shape of X_test : ", X_test.shape)
print("Shape of X_train : ", X_train.shape)
print("Shape of Y_train : ", Y_train.shape)
print("Shape of Y_test : ", Y_test.shape)


#-----------------------------------------
# 5. Feature Scaling
#-----------------------------------------

print("5. Feature Scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)

X_test_scaled = scalar.transform(X_test)

print("Scaled training data : ")
print(X_train_scaled[:5])


#-----------------------------------------
# 6. ANN / MLP Model Training
#-----------------------------------------

print("6. ANN Model Training")

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation='relu',
    solver='adam',
    max_iter=500,
    random_state=42
)

print(model)

print("Train the model")

model.fit(X_train_scaled, Y_train)

print("Model training completed")


#-----------------------------------------
# 7. Number of Iterations
#-----------------------------------------

print("7. Number of Iterations")

print("Number of iterations required : ", model.n_iter_)


#-----------------------------------------
# 8. Model Evaluation
#-----------------------------------------

print("8. Model Evaluation")

# Prediction
Y_pred = model.predict(X_test_scaled)

# Training accuracy
train_accuracy = accuracy_score(
    Y_train,
    model.predict(X_train_scaled)
)

# Testing accuracy
test_accuracy = accuracy_score(
    Y_test,
    Y_pred
)

print("Training Accuracy : ", train_accuracy)

print("Testing Accuracy : ", test_accuracy)


#-----------------------------------------
# 9. Confusion Matrix
#-----------------------------------------

print("9. Confusion Matrix")

cm = confusion_matrix(Y_test, Y_pred)

print(cm)


#-----------------------------------------
# 10. Prediction Probability
#-----------------------------------------

print("10. Prediction Probability")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])


#-----------------------------------------
# 11. Plot Loss Curve
#-----------------------------------------

print("11. Loss Curve")

plt.plot(model.loss_curve_)

plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.title("MLP Loss Curve")

plt.show()


#-----------------------------------------
# 12. Model Preservation
#-----------------------------------------

print("12. Model Preservation")

joblib.dump(model, "employee_attrition_mlp_model.pkl")
joblib.dump(scalar, "employee_attrition_scalar.pkl")

print("Model and Scalar saved successfully")


#-----------------------------------------
# 13. Load Model
#-----------------------------------------

print("13. Loading Model")

loaded_model = joblib.load("employee_attrition_mlp_model.pkl")
loaded_scalar = joblib.load("employee_attrition_scalar.pkl")

print("Model loaded successfully")


#-----------------------------------------
# 14. PredictAttrition Function
#-----------------------------------------

print("14. Predict Employee Attrition")


def PredictAttrition(employee):

    employee_scaled = loaded_scalar.transform([employee])

    prediction = loaded_model.predict(employee_scaled)

    probability = loaded_model.predict_proba(employee_scaled)

    print("Employee Data : ")
    print(employee)

    print("Prediction Probability : ")
    print(probability)

    if prediction[0] == 1:
        print("Prediction : Employee is likely to leave")
    else:
        print("Prediction : Employee is likely to stay")


#-----------------------------------------
# 15. Test New Employee
#-----------------------------------------

print("15. Test New Employee")


new_employee = [
    30,     # Age
    5000,   # MonthlyIncome
    5,      # YearsAtCompany
    8,      # TotalWorkingYears
    10,     # DistanceFromHome
    3,      # JobSatisfaction
    3,      # WorkLifeBalance
    1,      # OverTime (Yes = 1, No = 0)
    2,      # NumCompaniesWorked
    3       # TrainingTimesLastYear
]

PredictAttrition(new_employee)


#-----------------------------------------
# 16. Overfitting / Underfitting Check
#-----------------------------------------

print("16. Overfitting / Underfitting Check")

print("Training Accuracy : ", train_accuracy)
print("Testing Accuracy : ", test_accuracy)

if train_accuracy > 0.90 and train_accuracy - test_accuracy > 0.10:
    print("Model may be Overfitting")

elif train_accuracy < 0.70 and test_accuracy < 0.70:
    print("Model may be Underfitting")

else:
    print("Model has reasonable performance")