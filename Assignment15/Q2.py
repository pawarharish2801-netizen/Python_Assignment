def main():
    Length = int(input ("Enter the Length : "))
    List = []
    

    for i in range(Length):
        Num = int(input(f"Enter the Number {i+1} : "))
        List.append(Num)
    
    Ret = []
    Ret = list(filter( lambda NO : True if NO % 2 == 0 else False ,List  ))

    print(Ret)

if __name__ == ("__main__"):
    main()