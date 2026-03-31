import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split

def main():
    # Step 1 : Loading the dataset
    df = pd.read_csv('student_performance_ml .csv')

    # Step 2 : Train Test Split

    X = df.drop('FinalResult', axis = 1)
    Y = df['FinalResult']
    X_train , X_test ,Y_train , Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Step 3 : Model Building
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train,Y_train)

    # Step 4 : Prediction
    Y_pred = model.predict(X_test)

    # Step 5 : Accuracy Calculation
    acc = accuracy_score(Y_test,Y_pred)
    print("Accuracy Score is : ", acc*100 ,"%")

    # Step 6 : Confusion Matrix
    print("Confusion Matrix is : \n",confusion_matrix(Y_test,Y_pred))

    print("True Positive is Actual is pass and predicted is pass")
    print("True Negative is Actual is fail and predicted is fail")
    print("False Positive is Actual is fail and predicted is pass")
    print("False Negative is Actual is pass and predicted is fail")


   


if __name__ == "__main__": 
    main()