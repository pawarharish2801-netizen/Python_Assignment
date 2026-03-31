def DisplayPattern(iNo):

    for i in range (1 , iNo + 1):
        for j in range (1, i+1):
            print(j , end = " ")
        print()
    

def main():
    
    iNo = int(input("Enter First Number : "))

    DisplayPattern(iNo)

if __name__ ==("__main__"):
    main()