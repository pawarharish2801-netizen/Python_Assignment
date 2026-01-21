
def Arithmetic(iNo1, iNo2):
    Addition = iNo1 + iNo2
    Subtraction = iNo1 - iNo2
    Multiplication = iNo1 * iNo2
    Division = iNo1 / iNo2 if iNo2 != 0 else "Undefined (division by zero)"

    print("Addition: ", Addition)
    print("Subtraction: ", Subtraction)
    print("Multiplication: ", Multiplication)
    print("Division: ", Division)
   

def main():
    iNo1 = int(input("Enter first number: "))
    iNo2 = int(input("Enter second number: "))

    Arithmetic(iNo1, iNo2)

if __name__ == "__main__":
    main()   