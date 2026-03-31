
def DisplayReverse(iNo1):
   for i in range(iNo1 , 0 ,-1):
       print(i)
   


def main():
    iNo1 = int(input("Enter  number: "))

    DisplayReverse(iNo1)
    
if __name__ == "__main__":
    main()   