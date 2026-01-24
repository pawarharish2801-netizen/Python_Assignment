import threading

def Display():
    for i in range(1, 51):
        print(threading.current_thread().name, ":", i)

def DisplayReverse():
    for i in range(50, 0, -1):
        print(threading.current_thread().name, ":", i)

def main():

    Thread1 = threading.Thread(target=Display, name="Thread1")
    Thread2 = threading.Thread(target=DisplayReverse, name="Thread2")

    Thread1.start()
    Thread1.join()   # synchronization

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()
