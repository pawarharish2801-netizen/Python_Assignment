Max = lambda No1 , No2 , No3 : No1 if (No1 > No2 and No1 > No3) else (No2 if (No2 > No3) else No3)

def main():
    Num1 = int(input("Enter the Number 1 : "))
    Num2 = int(input("Enter the Number 2 : "))
    Num3 = int(input("Enter the Number 3 : "))

    Ret = Max(Num1 , Num2 , Num3)

    print("Multiplication of {0} and {1} is {2} : {3}".format(Num1 , Num2 ,Num3 ,Ret))

if __name__ == ("__main__"):
    main()