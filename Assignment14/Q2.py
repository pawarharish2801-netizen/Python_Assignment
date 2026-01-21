Cube = lambda num : num ** 3
def main():
    Num = int(input ("Enter the Number : "))

    print ("Square of {0} is : {1}".format(Num,Cube(Num)))
    
if __name__ == ("__main__"):
    main()