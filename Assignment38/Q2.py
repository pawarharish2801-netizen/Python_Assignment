import pandas as pd

def main():
    df = pd.read_csv('student_performance_ml .csv')

    print('Total no of students in dataset : ',df.shape[0])

    passed_count = (df['FinalResult'] == 1).sum()
    print('Total students who have passed  : ',passed_count)

    failed_count = (df['FinalResult'] == 0).sum()
    print('Total students who have failed  : ',failed_count)
if __name__ == "__main__":
    main()