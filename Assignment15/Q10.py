from functools import reduce

def main():
    Length = int(input("Enter the number of elements: "))
    List = []

    for i in range(Length):
        Num = int(input(f"Enter the Number {i+1}: "))
        List.append(Num)

    Ret = list(filter( lambda a : True if (a %2) == 0 else False , List))
    
    print(len(Ret))

if __name__ == "__main__":
    main()
