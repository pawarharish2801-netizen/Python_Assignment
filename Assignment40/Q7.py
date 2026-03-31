import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

def main():
    
    # Step 1 : Loading the dataset
    # Note: Removed the trailing space in the filename
    df = pd.read_csv('student_performance_ml .csv')

    # Step 2 : Train Test Split
    X = df.drop(['FinalResult'], axis = 1)
    Y = df['FinalResult']
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print(X.columns)
    # Step 3 : Model Building
    model1 = DecisionTreeClassifier(random_state=0)
    model2 = DecisionTreeClassifier(random_state=10)
    model3 = DecisionTreeClassifier(random_state=42)
    model1.fit(X_train, Y_train)
    model2.fit(X_train, Y_train)
    model3.fit(X_train, Y_train)

    # Step 4 : Predict
    Y_pred1 = model1.predict(X_test)
    Y_pred2 = model2.predict(X_test)
    Y_pred3 = model3.predict(X_test)
    # Step 5 : Accuracy Score

    Acc1 = accuracy_score(Y_test, Y_pred1)
    Acc2 = accuracy_score(Y_test, Y_pred2)
    Acc3 = accuracy_score(Y_test, Y_pred3)
    
    print("Accuracy of model with random_state=0 is : ", Acc1)
    print("Accuracy of model with random_state=10 is : ", Acc2)
    print("Accuracy of model with random_state=42 is : ", Acc3)

if __name__ == "__main__": 
    main()