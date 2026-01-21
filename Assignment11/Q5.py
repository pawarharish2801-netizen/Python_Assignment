

def CheckPalindrome(iNo1):
    iReverse = 0
    iDigit = 0
    iTemp = iNo1

    while(iNo1 !=0):

        iDigit = int(iNo1) % 10
        iReverse = (iReverse * 10) + iDigit
        iNo1  = int(iNo1 /10)

    if(iTemp == iReverse):
        return True
    else:
        return False

def main():
    iNo1 = int(input("Enter the Number : "))
    bRet = CheckPalindrome(iNo1)

    if bRet == True:    
        print(iNo1 , "is a Palindrome Number")
    else:
        print(iNo1 , "is not a Palindrome Number")

   

if __name__ =="__main__":
    main()


