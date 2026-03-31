import os

def main():
    try:
        filename = input("Enter filename: ")
        word = input("Enter word to search: ")
        
        if not os.path.exists(filename):
            print("Error: File does not exist")
            return
        
        with open(filename, 'r') as file:
            content = file.read()
        
        if word in content:
            print(f"Word '{word}' is found in {filename}")
        else:
            print(f"Word '{word}' is not found in {filename}")
    
    except PermissionError:
        print("Error: Permission denied")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()