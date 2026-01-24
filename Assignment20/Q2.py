import threading
def DisplayEven(no):

    for i in range (2 , int(no +1 / 2) , 2):
        if no % i == 0 :
            print("Even Factor : ",end = " ")
            print(i)
        

def DisplayOdd(no):
    
    for i in range (1 , int(no +1 / 2) , 2):
        if no % i == 0 :
            print("Odd Factor : ",end = " ")
            print(i)

        
def main():
    

    iNo = int(input("Enter the Number : "))

    EvenFactor = threading.Thread(target=DisplayEven , args= (iNo,) , name = "EvenFactor" )
    OddFactor = threading.Thread(target=DisplayOdd , args = (iNo,),name = "OddFactor") 

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()


if __name__ == "__main__":
    main()