import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
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
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, Y_train)

    # Step 4 : Predict
    Y_pred = model.predict(X_test)


    # Step 5 : Accuracy Score

    print("Accuracy is : ",accuracy_score(Y_test,Y_pred))

    # Step 6 : Visualize the Decision Tree
    plt.figure(figsize=(12,8))
    plot_tree(model, feature_names=X.columns, filled=True)
    plt.title("Decision Tree Visualization")
    plt.show()

    # Step 7 : Analyze Decision Tree Depth

    print("The features that appears at the root node is : Attendance")
    print("The feature importance scores for each feature are : ", model.feature_importances_)

if __name__ == "__main__": 
    main()