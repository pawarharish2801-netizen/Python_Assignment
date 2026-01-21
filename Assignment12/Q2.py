
def PrintFactor(iNo):
    
    for i in range(1, (iNo // 2) + 1):
        if (int(iNo % i ) == 0):
            print(i)
    
def main():
    
    iNo = int(input("Enter the Number : "))  

    PrintFactor(iNo)  

if __name__ == "__main__":
    main()