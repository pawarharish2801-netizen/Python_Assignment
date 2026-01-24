
from functools import reduce
def main():
    
    Len = int(input("Enter the Length : ")) 
    nums = []

    for i in range(Len):
        No = int(input(f"Enter No {i+1} : "))
        nums.append(No)
    
    Ret = list(filter(lambda a : True if a % 2 == 0 else False , nums))
    print(Ret)

    Ret = list(map(lambda a : a **2 , Ret))
    print(Ret)

    Ret = reduce(lambda a , b : a + b , Ret)
    print(Ret)

if __name__ == "__main__":
    main()