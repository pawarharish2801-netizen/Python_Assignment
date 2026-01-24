def DisplayPattern(n):

    for i in range (1,n+1):
        print("*"*n)

def main():
    iNo = int(input("Enter the number : "))

    DisplayPattern(iNo)

if __name__ == "__main__":
    main()