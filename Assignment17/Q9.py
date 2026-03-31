def CountDigit(iNo):

    Count = 0 

    if iNo == 0:
        return 1
    
    if iNo < 0 :
        iNo = -iNo
    
    while (iNo != 0):
        Count += 1
        iNo =int( iNo /10)
    
    return Count
        
def main():
    
    iNo = int(input("Enter Number : "))

    Ret = CountDigit(iNo)

    print("The No of Digits are : {0}".format(Ret))

if __name__ == "__main__":
    main()