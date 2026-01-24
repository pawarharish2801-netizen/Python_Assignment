def DisplayFactorial(no):
    iFact = 1 

    for i in range (1,no+1):
        iFact *= i

    return iFact
    
def main():
    iNo = int(input("Enter the number : "))

    Ret = DisplayFactorial(iNo)

    print("The factorial of {0} is :{1} ".format(iNo,Ret))

if __name__ == "__main__":
    main()