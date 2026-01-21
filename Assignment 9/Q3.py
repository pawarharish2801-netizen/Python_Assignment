
def DisplaySquare(iNo1):
    return iNo1 * iNo1

def main():
    iNo1   = 0 
    iRet   = 0

    print("Enter number:")
    iNo1 = int(input()) 

    iRet = DisplaySquare(iNo1)
    print("Square is:", iRet)

if __name__ == "__main__":
    main() 