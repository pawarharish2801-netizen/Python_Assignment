
def DisplayTable( iNo1):
    for i in range (1,11,1):
        print(iNo1 * i)

def main():
    iNo1 = int(input("Enter the Number : "))

    DisplayTable(iNo1)

if __name__ == "__main__":
    main()