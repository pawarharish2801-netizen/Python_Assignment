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
    model1 = DecisionTreeClassifier(random_state=42,max_depth=1)
    model2 = DecisionTreeClassifier(random_state=42,max_depth=3)
    model3 = DecisionTreeClassifier(random_state=42)
    
    model1.fit(X_train,Y_train)
    model2.fit(X_train,Y_train)
    model3.fit(X_train,Y_train)

    # Step 4 : Prediction
    Y_actual1 = model1.predict(X_train)
    Y_actual2 = model2.predict(X_train)
    Y_actual3 = model3.predict(X_train)

    Y_pred1 = model1.predict(X_test)
    Y_pred2 = model2.predict(X_test)
    Y_pred3 = model3.predict(X_test)

    # Step 5 : Accuracy Calculation
    Testingacc1 = accuracy_score(Y_test,Y_pred1)
    Testingacc2 = accuracy_score(Y_test,Y_pred2)
    Testingacc3 = accuracy_score(Y_test,Y_pred3)

    Trainingacc1 = accuracy_score(Y_train,Y_actual1)
    Trainingacc2 = accuracy_score(Y_train,Y_actual2)
    Trainingacc3 = accuracy_score(Y_train,Y_actual3)

    print("Model 1 with max_depth=1")
    print("Training Accuracy:", Trainingacc1)
    print("Testing Accuracy:", Testingacc1)

    print("Model 2 with max_depth=3")
    print("Training Accuracy:", Trainingacc2)
    print("Testing Accuracy:", Testingacc2)

    print("Model 3 with max_depth=None")
    print("Training Accuracy:", Trainingacc3)
    print("Testing Accuracy:", Testingacc3)
   
    print("All three models have same accuracy but model 1 is best as it is simple and less complex than other two models")
if __name__ == "__main__": 
    main()