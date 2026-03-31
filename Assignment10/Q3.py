
def DisplayFactorial (iNo1):
    iFact = 1 
    for i in range(1, iNo1 + 1, 1):
        iFact = iFact * i  
    return iFact
    
def main():
    iNo1 = int(input("Enter the Number : "))
    iRet = 0 
    
    iRet = DisplayFactorial(iNo1)

    print("Factorial of Numbers is :", iRet)

if __name__ == "__main__":
    main()