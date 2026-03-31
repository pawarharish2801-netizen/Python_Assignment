def Addition(A , B):
    return A + B

def main():
    Num1 = int(input("Enter the Number : "))
    Num2 = int(input("Enter the Number : "))

    Ret = Addition(Num1 , Num2)

    print("Addition of {0} and {1} is : {2}".format(Num1 , Num2 , Ret))

if __name__ == ("__main__"):
    main()