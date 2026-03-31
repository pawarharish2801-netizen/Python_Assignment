import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

def main():
    # Step 1 : Loading the dataset
    df = pd.read_csv('student_performance_ml .csv') 

    # Step 2 : Train Test Split
    X = df.drop('FinalResult', axis=1)
    Y = df['FinalResult']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Step 3 : Model Building
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, Y_train)

    # Step 4: Model Evaluation (Checking Accuracies)
    
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_accuracy = accuracy_score(Y_train, train_predictions) * 100
    test_accuracy = accuracy_score(Y_test, test_predictions) * 100

    print("--- Model Accuracies ---")
    print(f"Training Accuracy: {train_accuracy:.2f}%")
    print(f"Testing Accuracy: {test_accuracy:.2f}%\n")

    student_marks = pd.DataFrame(
        [[6, 85, 66, 7, 7]], 
        columns=['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']
    )
    
    result = model.predict(student_marks)
    
    if result[0] == 1:
        print("The model predicts the student will: PASS (1)")
    else:
        print("The model predicts the student will: FAIL (0)")

if __name__ == "__main__": 
    main()