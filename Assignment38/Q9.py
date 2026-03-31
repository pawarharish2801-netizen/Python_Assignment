import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('student_performance_ml .csv')

    plt.figure(figsize=(8,5))
    plt.plot(df['FinalResult'] ,df['AssignmentsCompleted'] )
    plt.xlabel('Final Result`')
    plt.ylabel('Assignments Completed')
    plt.title('Assignments Completed vs Final Result')
    plt.show()

    print("Study says that students who have completed more assignments are more likely to pass the final exam.")
    
    



   
if __name__ == "__main__":
    main()