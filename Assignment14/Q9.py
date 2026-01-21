Multiplication = lambda No1 , No2 :  No1 * No2 

def main():
    Num1 = int(input("Enter the Number 1 : "))
    Num2 = int(input("Enter the Number 2 : "))

    Ret = Multiplication(Num1 , Num2)

    print("Multiplication of {0} and {1} is : {2}".format(Num1 , Num2 , Ret))

if __name__ == ("__main__"):
    main()