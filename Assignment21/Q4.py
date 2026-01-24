import threading

# Shared variables
result = {
    "sum": 0,
    "product": 1
}

def SumElements(arr):
    total = 0
    for num in arr:
        total += num
    result["sum"] = total
    print(threading.current_thread().name, "calculated sum")

def ProductElements(arr):
    prod = 1
    for num in arr:
        prod *= num
    result["product"] = prod
    print(threading.current_thread().name, "calculated product")

def main():

    size = int(input("Enter number of elements : "))
    arr = []

    print("Enter elements :")
    for i in range(size):
        arr.append(int(input()))

    t1 = threading.Thread(target=SumElements, args=(arr,), name="Thread1")
    t2 = threading.Thread(target=ProductElements, args=(arr,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nResults in Main Thread")
    print("Sum of elements :", result["sum"])
    print("Product of elements :", result["product"])

if __name__ == "__main__":
    main()
