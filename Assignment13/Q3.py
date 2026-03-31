
def ChkPerfect(num):
    sum_divisors = 0

    for i in range(1, int(num)):
        if int((num % i)) == 0:
            sum_divisors = sum_divisors + i

    if sum_divisors == num:
         return True
    else:
        return False

def main():
    num = int(input("Enter a number: "))

    bRet = ChkPerfect(num)
    if bRet == True:
        print("The number is perfect.")
    else:
        print("The number is not perfect.")
if __name__ == "__main__":
    main()      