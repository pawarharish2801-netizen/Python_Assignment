import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('student_performance_ml .csv')

    plt.figure(figsize=(8,5))
    plt.hist(df['StudyHours'])
    plt.show()
    
    print("Study says that most student study more than 4 hours ")
    



   
if __name__ == "__main__":
    main()