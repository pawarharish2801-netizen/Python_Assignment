
def DisplayOdd (iNo1):
    
    for i in range(1, iNo1 + 1, 2):
        print(i)
    
    
def main():
    iNo1 = int(input("Enter the Number : "))
    
    DisplayOdd(iNo1)

if __name__ == "__main__":
    main()