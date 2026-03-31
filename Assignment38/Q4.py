import pandas as pd

def main():
    df = pd.read_csv('student_performance_ml .csv')

    print(df.value_counts(df['FinalResult']))

    passed_percentage = ((df['FinalResult'] == 1).sum())/df.shape[0]
    print("Passed Percentage is : ",passed_percentage)

    Failed_percentage = ((df['FinalResult'] == 0).sum())/df.shape[0]
    print("Failed Percentage is : ",Failed_percentage)

    print("Dataset is not balanced as passed percentage is 0.6 and failed percentage is 0.4 ")
    



   
if __name__ == "__main__":
    main()