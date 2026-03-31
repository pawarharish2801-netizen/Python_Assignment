
def CheckPrime(iNo1):

    for i in range (2 , (int((iNo1+1)/2))):
        #FILTER
        if ( iNo1 == 1):
            return False
        
        iNo1 = iNo1 / i
        if (iNo1 % i == 0):
            return False
    return True        

def main():
    iNo1 = int(input("Enter the Number : "))
    bRet = CheckPrime(iNo1)

    if bRet == True:
        print(iNo1 , "is a Prime Number")   
    else:
        print(iNo1 , "is not a Prime Number")

if __name__ =="__main__":
    main()