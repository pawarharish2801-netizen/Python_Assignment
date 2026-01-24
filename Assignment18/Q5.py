import MarvellousNum

def ListPrime(arr):

    Sum = 0

    for num in arr:
        if MarvellousNum.ChkPrime(num):
            Sum += num

    return Sum

def main():

    size = int(input("Enter number of elements : "))
    arr = []

    print("Enter the elements :")
    for i in range(size):
        arr.append(int(input()))

    Ret = ListPrime(arr)
    print("Output :", Ret)


if __name__ == "__main__":
    main()
