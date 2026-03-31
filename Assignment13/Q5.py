def DisplayGrade(no):
    if (no>=75):
        print("Distinction")
    elif (no>=60):
        print("First Class")
    elif (no>=50):
        print("Second Class")
    elif (no<50):
        print("Fail")

    
def main():
    num = int(input("Enter a number: "))

    DisplayGrade(num)

if __name__ == "__main__":
    main()      