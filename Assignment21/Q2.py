import threading

def DisplayMax(arr):
    print(threading.current_thread().name, "Maximum element is :", max(arr))

def DisplayMin(arr):
    print(threading.current_thread().name, "Minimum element is :", min(arr))

def main():

    size = int(input("Enter number of elements : "))
    arr = []

    print("Enter elements :")
    for i in range(size):
        arr.append(int(input()))

    t1 = threading.Thread(target=DisplayMax, args=(arr,), name="Thread1")
    t2 = threading.Thread(target=DisplayMin, args=(arr,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
