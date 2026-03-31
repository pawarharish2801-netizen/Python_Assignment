import pandas as pd

def main():
    df = pd.read_csv('student_performance_ml .csv')

    print('first 5 records are : \n',df.head())
    print('last 5 records are : \n',df.tail())
    print('Shape of the csv is : ',df.shape)
    print('Column names are : \n',df.columns)
    print('Datatype of each columns are : ',df.dtypes)

if __name__ == "__main__":
    main()