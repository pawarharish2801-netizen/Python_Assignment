
def Addition(iNo):
    Sum = 0 

    for i in range(len(iNo)):
        Sum += iNo[i]
    
    return Sum

from functools import reduce
def main():
    
    Len = int(input("Enter the Length : ")) 
    nums = []

    for i in range(Len):
        No = int(input(f"Enter No {i+1} : "))
        nums.append(No)

    ret = Addition(nums)

    print("The Addition is : {0}".format(ret))
    
    

if __name__ == "__main__":
    main()