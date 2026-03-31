
def ReverseDigit(iNo1):
    iDigit = 0
    iRev = 0

    while(iNo1 !=0):

        iDigit = int(iNo1) % 10
        iRev = iRev * 10 + iDigit
        iNo1 = int(iNo1 / 10)

    return iRev

def main():
    iNo1 = int(input("Enter the Number : "))

    iRet = ReverseDigit(iNo1)

    print("The Reverse of the Digit are : ",iRet)
    

   

if __name__ =="__main__":
    main()


