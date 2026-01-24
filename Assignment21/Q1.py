def ChkPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

import threading

def DisplayPrime(arr):
    print(threading.current_thread().name, "numbers:")
    for num in arr:
        if ChkPrime(num):
            print(num, end=" ")
    print()


def DisplayNonPrime(arr):
    print(threading.current_thread().name, "numbers:")
    for num in arr:
        if not ChkPrime(num):
            print(num, end=" ")
    print()

def main():

    size = int(input("Enter number of elements : "))
    arr = []

    print("Enter elements :")
    for i in range(size):
        arr.append(int(input()))

    t1 = threading.Thread(target=DisplayPrime, args=(arr,), name="Prime")
    t2 = threading.Thread(target=DisplayNonPrime, args=(arr,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
