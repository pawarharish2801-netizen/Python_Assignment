import os 
import sys

def Script(FName, Ext):
    try:
        if  os.path.isdir(FName) == False:
            print("Error: The path mentioned is not a directory")
            return
        
        
        filelist = os.listdir(FName)
        
        filtered_files = list(filter(lambda file: file.endswith(Ext), filelist))
        
        if len(filtered_files) == 0:
            print(f"No files found with extension '{Ext}' in {FName}")
        else:
            print(f"Files with extension '{Ext}' in {FName}:")
            for file in filtered_files:
                print(file)
    
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) == 3 :
        Script(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python FileName <DirectoryName> <extension>")

if __name__ == "__main__":
    main()