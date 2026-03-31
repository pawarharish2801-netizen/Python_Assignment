import pandas as pd

def main():
    df = pd.read_csv('student_performance_ml .csv')

    average_studyhour = df['StudyHours'].mean()
    print('Average study hour : ',average_studyhour)

    average_Attendance = df['Attendance'].mean()
    print('Average Attendance : ',average_Attendance)

    average_PreviousScore = df['PreviousScore'].mean()
    print('Average PreviousScore : ',average_PreviousScore)

    average_SleepHours = df['SleepHours'].mean()
    print('Average SleepHours : ',average_SleepHours)




   
if __name__ == "__main__":
    main()