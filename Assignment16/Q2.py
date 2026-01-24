def ChkNumber(No):
    if No % 2 == 0:
        print("The Number {} is Even".format(No))
    else:
        print("The Number {} is Odd".format(No))

def main():
    Num = int(input("Enter the Number : "))
    ChkNumber(Num)

if __name__ == ("__main__"):
    main()