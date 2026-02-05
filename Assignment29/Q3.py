import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_file> <destination_file>")
        return
    
    source_file = sys.argv[1]
    dest_file = sys.argv[2]
    
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not not exist")
        return
    
    try:
        fSource = open(source_file , 'r')
        Data = fSource.read()

        fDest = open(dest_file,'w')
        fDest.write(Data)
        
        print(f"Successfully copied '{source_file}' to '{dest_file}'")
    
    except PermissionError:
        print(f"Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()