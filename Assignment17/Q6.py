def DisplayPattern(iNo):

    for i in range (iNo , 0 , -1):
        print("*"*i)


def main():
    
    iNo = int(input("Enter First Number : "))

    DisplayPattern(iNo)

if __name__ ==("__main__"):
    main()