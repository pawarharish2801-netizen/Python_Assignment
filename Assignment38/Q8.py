import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('student_performance_ml .csv')

    plt.figure(figsize=(8,5))
    plt.boxplot(df['Attendance'])
    plt.show()
    
    print('No outliers are present')
    



   
if __name__ == "__main__":
    main()