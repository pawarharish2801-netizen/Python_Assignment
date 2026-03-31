

def DcimalToBinary(num):
    binArr = []
    str = 0 

    while num > 0 :
        str = int(num % 2)
        binArr.append(str)
        num = int(num / 2) 
    
    binArr.reverse() 
    print(binArr)

    
def main():
    num = int(input("Enter a number: "))

    DcimalToBinary(num)

if __name__ == "__main__":
    main()      