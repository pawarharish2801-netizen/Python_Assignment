
from functools import reduce

def main():
    
    Len = int(input("Enter the Length : ")) 
    nums = []

    for i in range(Len):
        No = int(input(f"Enter No {i+1} : "))
        nums.append(No)
    
    Ret = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)), nums))
    print(Ret)

    Ret = list(map(lambda a : a *2 , Ret))
    print(Ret)

    Ret = reduce(lambda a , b : a if a > b else b , Ret)
    print(Ret)

if __name__ == "__main__":
    main()