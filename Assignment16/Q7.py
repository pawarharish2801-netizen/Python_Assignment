def ChkNumber(No):
    if (No > 0):
        print("The Number {} is Positive".format(No))
    elif (No < 0):
        print("The Number {} is Negative".format(No))
    else:
        print("The Number is Zero".format(No))
def main():
    Num = int(input("Enter the Number : "))

    ChkNumber(Num)

if __name__ == ("__main__"):
    main()