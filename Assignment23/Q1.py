
class Bookstore:
    No_Of_Books = 0 

    def __init__(self, Name , Author):
        self.Name = Name
        self.Author = Author
        Bookstore.No_Of_Books +=1
    
    def Display(self):
        print("Name : ",self.Name)
        print("Author : ",self.Author)

Obj1 = Bookstore("Linux System Programming", "Robert Love")
Obj1.Display()
# Linux System Programming by Robert Love. No of books: 1

print ("-------------------------------------------------------------------------------")
Obj2 = Bookstore("C Programming", "Dennis Ritchie")
Obj2.Display()
# C Programming by Dennis Ritchie. No of books: 2
