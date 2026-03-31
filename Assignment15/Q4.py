from functools import reduce

def main():
    Length = int(input("Enter the number of elements: "))
    List = []

    for i in range(Length):
        Num = int(input(f"Enter the Number {i+1}: "))
        List.append(Num)

    Ret = reduce(lambda a, b: a + b, List)
    print("Addition of all numbers is:", Ret)

if __name__ == "__main__":
    main()
