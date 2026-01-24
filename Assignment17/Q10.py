def CountDigit(iNo):

    Sum = 0 
    Digit = 0 

    if iNo == 0:
        return 1
    
    if iNo < 0 :
        iNo = -iNo
    
    while (iNo != 0):
        Digit = int(iNo % 10)
        Sum = Sum + Digit
        iNo =int( iNo /10)
    
    return Sum
        
def main():
    
    iNo = int(input("Enter Number : "))

    Ret = CountDigit(iNo)

    print("The Sum of Digits are : {0}".format(Ret))

if __name__ == "__main__":
    main()