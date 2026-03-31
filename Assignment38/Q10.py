import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('student_performance_ml .csv')

    plt.figure(figsize=(8,5))
    plt.plot(df['FinalResult'] ,df['SleepHours'] )
    plt.xlabel('Final Result`')
    plt.ylabel('Sleeping Hours')
    plt.title('Sleeping Hours vs Final Result')
    plt.show()

    print("Study says that students who sleep more hours are more likely to pass the final exam.")
   



   
if __name__ == "__main__":
    main()