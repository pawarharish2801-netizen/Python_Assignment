
def Frequency(iNo , iValue):
    Count = 0  

    for i in range(len(iNo)):
        if (iNo[i] == iValue):
            Count +=1

    return Count

from functools import reduce
def main():
    
    Len = int(input("Enter the Length : ")) 
    nums = []

    for i in range(Len):
        No = int(input(f"Enter No {i+1} : "))
        nums.append(No)

    Value = int(input("Enter the Number you want to find : "))
    ret = Frequency(nums,Value)

    print("The Frequency is : {0}".format(ret))
    
    

if __name__ == "__main__":
    main()