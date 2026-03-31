
class Demo:

    Value = 0 
    def __init__(self,A,B):
        self.No1 = A 
        self.No2 = B

    def Fun(self): 
        print("Inside Fun Method of Demo : ",self.No1 , self.No2)
    
    def Gun(self):
        print("Inside Gun Method of Demo : ",self.No1 , self.No2)

def main():
    
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()



if __name__ == "__main__":
    main()