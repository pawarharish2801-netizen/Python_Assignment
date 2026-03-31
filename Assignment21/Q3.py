import threading

No = 0
lock = threading.Lock()

def Count():
    global No
    for i in range(15):
        with lock:   # acquire + release automatically
            No += 1
            print(threading.current_thread().name, ":", No)
            

t1 = threading.Thread(target=Count, name="t1")
t2 = threading.Thread(target=Count, name="t2")

t1.start()
t2.start()

t1.join()
t2.join()

print("The final value of counter is :", No)
