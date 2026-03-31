
def CountSum(iNo1):
    
    iSum = 0
    iDigit = 0
    
    while(iNo1 !=0):
    
        iDigit = int(iNo1) % 10
        iSum = iSum + iDigit
        iNo1  = int(iNo1 /10)
    
    return iSum


def main():
    iNo1 = int(input("Enter the Number : "))

    iRet = CountSum(iNo1)

    print("The no of Sum are : ",iRet)
   

if __name__ =="__main__":
    main()