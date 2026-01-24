def ChkPrime(no):

    for i in range(2,int((no+1)/2)):
        if no % i == 0:
            return False

    return True


def main():
    iNo = int(input("Enter the number : "))

    bRet = ChkPrime(iNo)

    if bRet == True :
        print("The no {0} is prime number .".format(iNo))
    else:
        print("The no {0} is not prime number .".format(iNo))

if __name__ == "__main__":
    main()