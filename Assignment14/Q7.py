ChkDivisible = lambda No : True if (int(No % 5) == 0) else False

def main():
    Num = int(input("Enter the Number : "))

    bRet = ChkDivisible(Num)

    if bRet == True:
        print("The Number {0} is Divisible by 5".format(Num))
    else:
        print("The Number {0} is Not Divisible by 5".format(Num))

if __name__ == ("__main__"):
    main()