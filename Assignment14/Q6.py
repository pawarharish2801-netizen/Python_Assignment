chkEven = lambda Num : True if(int(Num % 2 ) != 0) else False

def main():
    Num1 = int(input ("Enter the Number : "))
    
    bRet = chkEven(Num1)

    if bRet == True:
        print("The Number {0} is Odd ".format(Num1))
    else:
        print("The Number {0} is Even ".format(Num1))


  

    
   
    
    
if __name__ == ("__main__"):
    main()