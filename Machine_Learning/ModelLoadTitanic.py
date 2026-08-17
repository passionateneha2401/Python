import pandas as pd
import joblib

def LoadModel(FileName):
    model = joblib.load(FileName)

    print("Model Loaded Successfully!")

    print(model.feature_names_in_)

    return model

def PredictPassenger(model):
    print("Enter the Informatiion")

    Pclass = int(input("Enter Pclass(1/2/3)"))
    Sex = int(input("Enter Sex : (0-female / 1-male)"))
    Age = int(input("Enter Age : "))
    sibsp = int(input("Enter siblings and spouse "))
    Parch = int(input("Enter Parent and child"))
    Fare = int(input("Enter Pclass(1/2/3)"))
    Embarked = float(input("Enter embarked(0/1/3))"))

    Passenger = pd.DataFrame([{
        "Pclass" : Pclass,
        "Sex": Sex,
        "Age" : Age,
        "sibsp" : sibsp,
        "Parch" : Parch,
        "Fare" : Fare,
        "Embarked" : Embarked
    }]) 

    Passenger = Passenger[model.feature_names_in_]
    result = model.predict(Passenger)

    print(result)

def main():
    model = LoadModel("MarvellousTitanic.pkl")
    PredictPassenger(model)

if __name__ == "__main__":
    main()