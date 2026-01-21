
def DisplaySum(iNo1):
    iSum = 0
    for i in range(1, iNo1 + 1, 1):
        iSum = iSum + i
    return iSum
    
def main():
    iNo1 = int(input("Enter the Number : "))
    iRet = 0 
    
    iRet = DisplaySum(iNo1)

    print("Sum of Numbers is :", iRet)

if __name__ == "__main__":
    main()