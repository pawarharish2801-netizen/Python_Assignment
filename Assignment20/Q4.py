import threading

def CountSmall(Brr):
    
    print(threading.get_ident())
    iCount = 0 
    for i in range (len(Brr)):
        if Brr[i] >= 'a' and Brr[i] <='z':
            iCount += 1
    print("The Small Characters of thread id {0} and name {1}: {2} ".format(threading.get_ident(),threading.current_thread().name, iCount))


def CountCapital(Brr):
    
    iCount = 0 
    for i in range (len(Brr)):
        if Brr[i] >= 'A' and Brr[i] <='Z':
            iCount += 1
    print("The Capital Characters  of thread id {0} and name {1}: {2} ".format(threading.get_ident(),threading.current_thread().name, iCount))

def CountDigits(Brr):

    iCount = 0 
    for i in range (len(Brr)):
        if Brr[i] >= '0' and Brr[i] <='9':
            iCount += 1
    
    print("The Digits of thread id {0} and name {1}: {2} ".format(threading.get_ident(),threading.current_thread().name, iCount))
        
def main():
    
    Arr = list(input("Enter the string : "))
    

    Small = threading.Thread(target=CountSmall , args= (Arr,) , name = "Small" )
    Capital = threading.Thread(target=CountCapital , args = (Arr,), name = "Capital") 
    Digits = threading.Thread(target =CountDigits , args= (Arr,), name = "Digits")

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()


if __name__ == "__main__":
    main()