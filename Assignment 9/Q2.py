
def CheckGreater(iNo1, iNo2):
    if (iNo1 > iNo2):
        return iNo1 
    else:
        return iNo2
def main():
    iNo1 = 0 
    iNo2 = 0
    iRet = 0 

    iNo1 = int(input("Enter first number: "))
    iNo2 = int(input("Enter second number: "))

    iRet = CheckGreater(iNo1, iNo2)

    print("Greater number is:", iRet)

        
    
if __name__ == "__main__":
    main()