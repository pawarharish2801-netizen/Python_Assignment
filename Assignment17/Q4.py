def DisplayFactSum(no):
    iSum = 0

    for i in range(1, no):
        if no % i == 0:
            iSum += i

    return iSum


def main():
    iNo = int(input("Enter the number : "))

    Ret = DisplayFactSum(iNo)

    print("The FactSum of {0} is :{1} ".format(iNo,Ret))

if __name__ == "__main__":
    main()