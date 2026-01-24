
def Maximum(iNo):
    Sum = 0 

    iMax = iNo[0]
    for i in range(len(iNo)):
        if (iNo[i] > iMax):
            iMax = iNo[i]

    
    return iMax

from functools import reduce
def main():
    
    Len = int(input("Enter the Length : ")) 
    nums = []

    for i in range(Len):
        No = int(input(f"Enter No {i+1} : "))
        nums.append(No)

    ret = Maximum(nums)

    print("The Maximum is : {0}".format(ret))
    
    

if __name__ == "__main__":
    main()