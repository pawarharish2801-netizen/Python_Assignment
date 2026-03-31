
def DisplayCube(iNo1):
    return iNo1 ** 3

def main():
    iNo1   = 0 
    iRet   = 0

    print("Enter number:")
    iNo1 = int(input()) 

    iRet = DisplayCube(iNo1)
    print("Cube is:", iRet)

if __name__ == "__main__":
    main() 