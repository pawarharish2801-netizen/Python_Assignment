min = lambda num1 , num2 : num1 if (num1 < num2) else num2

def main():
    Num1 = int(input ("Enter the Number : "))
    Num2 = int(input ("Enter the Number : "))

    Ret = min(Num1 , Num2)

    print ("Maximum between {0} and {1} is : {2}".format(Num1,Num2,Ret))

    
   
    
    
if __name__ == ("__main__"):
    main()