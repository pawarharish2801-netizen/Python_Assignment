
import threading
def DisplayEven():
    print("Inside Even")
    Even = 0
    for i in range (10):
        
        Even = Even + 2
        print(Even)

def DisplayOdd():
    
    print("Inside Odd")
    Odd = 1
    for i in range (10):

        print(Odd)
        Odd = Odd + 2

        
def main():
    
    Even = threading.Thread(target=DisplayEven , name = "Even")
    Odd = threading.Thread(target=DisplayOdd , name = "Odd") 

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()


if __name__ == "__main__":
    main()