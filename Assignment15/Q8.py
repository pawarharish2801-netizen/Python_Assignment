from functools import reduce

def main():
    Length = int(input("Enter the number of elements: "))
    List = []

    for i in range(Length):
        Num = int(input(f"Enter the Number {i+1}: "))
        List.append(Num)

    Ret = list(filter(lambda NO : True if (NO % 3 == 0 or NO % 5 == 0) else False ,List  ))

    print(Ret)

if __name__ == "__main__":
    main()
