import os

def main():
    try:
        filename = input("Enter filename: ")
        
        if (os.path.exists(filename) == False ):
            print("Error: File does not exist")
            return
        
        file = open(filename, 'r') 
        Data = file.readlines()

        for line in Data:
            print(line, end='')


    
    except PermissionError:
        print("Error: Permission denied")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()