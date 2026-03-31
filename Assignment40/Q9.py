import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main():
    
    # Step 1 : Loading the dataset
    df = pd.read_csv('student_performance_ml .csv')

    df['PerformanceIndex'] = (df['StudyHours'] * 2) + df['Attendance']
    
    # Step 2 : Train Test Split
    X = df.drop(['FinalResult'], axis=1)
    Y = df['FinalResult']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Step 3 : Model Building
    model = DecisionTreeClassifier(random_state=42, max_depth=12)
    model.fit(X_train, Y_train)

    # Step 4 : Checking the new accuracies
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_accuracy = accuracy_score(Y_train, train_predictions) * 100
    test_accuracy = accuracy_score(Y_test, test_predictions) * 100

    print("--- Accuracies WITH PerformanceIndex ---")
    print(f"Training Accuracy: {train_accuracy:.2f}%")
    print(f"Testing Accuracy: {test_accuracy:.2f}%")

    # Step 5 : Analyze the impact of the new feature
    print("\n--- Feature Importance ---")
    feature_importances = model.feature_importances_
    feature_names = X.columns
    importance_dict = dict(zip(feature_names, feature_importances))
    sorted_importance = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)
    for feature, importance in sorted_importance:
        print(f"{feature}: {importance:.4f}")


if __name__ == "__main__": 
    main()