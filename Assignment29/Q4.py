import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <first_file> <sec_file>")
        return
    
    first_file = sys.argv[1]
    sec_file = sys.argv[2]
    
    if not os.path.exists(first_file):
        print(f"Error: first file '{first_file}' does not not exist")
        return
    
    if not os.path.exists(sec_file):
        print(f"Error: Second file '{sec_file}' does not not exist")
        return
    
    try:
        f1 = open(first_file , 'r')
        f2 = open (sec_file , 'r')

        Data1 = f1.read()
        Data2 = f2.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")
        
    
    except PermissionError:
        print(f"Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()