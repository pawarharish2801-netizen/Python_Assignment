import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split

def main():
    
    # Step 1 : Loading the dataset
    df = pd.read_csv('student_performance_ml .csv')

    #Step 2 : Data Analysis

    print("First few records of the table : \n",df.head())
    print("Shape of table is : ",df.shape)
    print("Total Records in the table are : ",df.shape[0])


    # Step 3 : Train Test Split

    X = df.drop('FinalResult', axis = 1)
    Y = df['FinalResult']
    X_train , X_test ,Y_train , Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Step 4 : Model Building
    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)

    # Step 5 : Prediction
    Y_pred = model.predict(X_test)

    for i in range(len(Y_test)):
        print("Actual Result : ",Y_test.iloc[i], " Predicted Result : ",Y_pred[i])  


if __name__ == "__main__": 
    main()