from Arithmetic import *

def main():

    iNo1 = int(input("Enter first number: "))
    iNo2 = int(input("Enter second number: "))

    print("Addition:", add(iNo1, iNo2))
    print("Subtraction:", subtract(iNo1, iNo2))
    print("Multiplication:", multiply(iNo1, iNo2))
    print("Division:", divide(iNo1, iNo2))

if __name__ == "__main__":
    main()
