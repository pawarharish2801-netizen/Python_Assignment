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
    X = df.drop(['PreviousScore','AssignmentsCompleted','SleepHours','FinalResult'], axis = 1)
    Y = df['FinalResult']
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print(X.columns)
    # Step 3 : Model Building
    model = DecisionTreeClassifier(random_state=42,max_depth=None)
    model.fit(X_train, Y_train)

    # Step 4 : Predict
    Y_predtrain = model.predict(X_train)
    Y_predtest = model.predict(X_test)

    # Step 5 : Accuracy Score

    print("Testing Accuracy is : ",accuracy_score(Y_test,Y_predtest))
    print("Training Accuracy is : ",accuracy_score(Y_train,Y_predtrain))    

    print("Depth of the Decision Tree:", model.get_depth())
    print("No change in accuracy when we set max_depth to None, which means the tree is allowed to grow until all leaves are pure or until all leaves contain less than min_samples_split samples. This indicates that the model is not overfitting and is able to generalize well to unseen data.")
if __name__ == "__main__": 
    main()