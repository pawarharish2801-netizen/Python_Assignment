class Numbers:

    def __init__(self, no):
        self.Value = no

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print(f"Factors of {self.Value} are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False
def main():
    obj1 = Numbers(28)
    obj2 = Numbers(17)

    print("Object 1:")
    print("Prime:", obj1.ChkPrime())
    print("Perfect:", obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors:", obj1.SumFactors())

    print("\nObject 2:")
    print("Prime:", obj2.ChkPrime())
    print("Perfect:", obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors:", obj2.SumFactors())


if __name__ == "__main__":
    main()
