
def ChkDivisibleby3or5(iValue):
    if (iValue % 3 == 0) or (iValue % 5 == 0):
        return True
    else:
        return False
def main():
    iNo1   = 0 
    iRet   = 0

    print("Enter number:")
    iNo1 = int(input()) 

    iRet = ChkDivisibleby3or5(iNo1)

    if iRet == True:
        print(f"{iNo1} is divisible by 3 or 5") 
    else:
        print(f"{iNo1} is not divisible by 3 or 5")

if __name__ == "__main__":
    main() 