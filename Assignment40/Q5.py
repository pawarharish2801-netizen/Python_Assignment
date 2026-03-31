import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

def main():
    
    # Step 1 : Loading the dataset

    df = pd.read_csv('student_performance_ml .csv')

    # Step 2 : Train Test Split
    X = df.drop(['FinalResult'], axis = 1)
    Y = df['FinalResult']
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print(X.columns)
    # Step 3 : Model Building
    model = DecisionTreeClassifier(random_state=42,max_depth=12)
    model.fit(X_train, Y_train)

    # Step 4 : Making new Dataframe for prediction
    new_data = {
        'StudyHours' : [3,9,6,8,12],
        'Attendance': [40, 70, 95, 80, 90],
        'PreviousScore': [85,67,51,90,56],
        'AssignmentsCompleted': [10,11,7,2,4],
        'SleepHours': [7,6,6,9,5],
        'FinalResult' : [0,1,1,1,1]
    }
    new_df = pd.DataFrame(new_data)
    X_new = new_df.drop('FinalResult',axis =1)
    Y_new = new_df['FinalResult']

    Y_pred = model.predict(X_new)
    print(Y_pred)

    # Step 5 : Accuracy Score
    
    Correct = 0 
    iter = 0
    for i , j in zip(Y_new,Y_pred):
        iter +=1
        if i == j:
            Correct +=1 

    Acc = (Correct / iter)*100 
    print("Accuracy Score is :" , Acc)

if __name__ == "__main__": 
    main()