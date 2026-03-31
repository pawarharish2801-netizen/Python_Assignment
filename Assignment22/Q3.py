class Arithemetic:
    PI = 3.14 

    def __init__(self,A,B):
        self.Val1 = A
        self.Val2 = B

    def Addition(self):
        return self.Val1 + self.Val2
    
    def Substraction(self):
        return self.Val1 - self.Val2
    
    def Multiplication(self):
        return self.Val1 * self.Val2

    def Division(self):
        return self.Val1 / self.Val2

obj1 = Arithemetic(2,3)

Ret = obj1.Addition()
print("Addition : ",Ret)

Ret = obj1.Substraction()
print("Substraction : ",Ret)

Ret = obj1.Multiplication()
print("Multiplication : ",Ret)

Ret = obj1.Division()
print("Division : ",Ret)

print("-------------------------------------------------")
obj2 = Arithemetic(3,4)

Ret = obj2.Addition()
print("Addition : ",Ret)

Ret = obj2.Substraction()
print("Substraction : ",Ret)

Ret = obj2.Multiplication()
print("Multiplication : ",Ret)

Ret = obj2.Division()
print("Division : ",Ret)


