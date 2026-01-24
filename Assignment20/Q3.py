import threading
def DisplayEven(Brr):

    Sum = 0
    for i in range (len(Brr)):
        if Brr[i] % 2 == 0 :
            Sum = Sum + Brr[i]   

    print("The Sum of Even is : {0}".format(Sum))  

def DisplayOdd(Brr):
    Sum = 0
    for i in range (len(Brr)):
        if Brr[i] % 2 != 0 :
            Sum = Sum + Brr[i]   

    print("The Sum of Odd is : {0}".format(Sum)) 
    
   
        
def main():
    
    No = 0 
    Len = int(input("Enter the Elements : "))
    Arr = []

    for i in range(Len):
        No = int(input(f"Enter the no {i+1} : "))
        Arr.append(No)

    EvenList = threading.Thread(target=DisplayEven , args= (Arr,) , name= "EvenList" )
    OddList = threading.Thread(target=DisplayOdd , args = (Arr,) , name = "OddList") 

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()


if __name__ == "__main__":
    main()