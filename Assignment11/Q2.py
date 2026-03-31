
def CountDigits(iNo1):
    iCount = 0 ; 
    
    while(iNo1 !=0):
    
        
        iCount = iCount + 1
        iNo1  = int(iNo1 /10)
    
    return iCount


def main():
    iNo1 = int(input("Enter the Number : "))

    iRet = CountDigits(iNo1)

    print("The no of digits are : ",iRet)
   

if __name__ =="__main__":
    main()