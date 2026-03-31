def main():
    user_input = int(input("Enter strings separated by spaces: "))

    List = user_input.split()

    Ret = list(filter(lambda s: len(s) > 5, List))

    print(Ret)

if __name__ == "__main__":
    main()
