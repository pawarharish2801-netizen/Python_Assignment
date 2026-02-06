import os 
import sys
import time

def Script(FName, ext1, ext2):
    iCount = 0 
    Border = "-"*60


    try:
        if not os.path.isdir(FName):
            print("Error: The path mentioned is not a directory")
            return
        
        timestamp = time.ctime()
        LogFileName = "Q2%s.log" %(timestamp)
        LogFileName = LogFileName.replace(" ","_")
        LogFileName = LogFileName.replace(":","_")


        filelist = os.listdir(FName)
        
        filtered_files = list(filter(lambda file: file.endswith(ext1), filelist))
        
        if len(filtered_files) == 0:
            print(f"No files found with extension '{ext1}' in {FName}")
        else:
            for file in filtered_files:
                old_path = os.path.join(FName, file)
                
                new_name = file.replace(ext1, ext2)
                
                new_path = os.path.join(FName, new_name)
                
                os.rename(old_path, new_path)
                iCount += 1
            print("File Extension Changed Successfully :-) ")
            
                
        fd = open(LogFileName,'w')
        print("Log Report Generated at :" + os.path.abspath(LogFileName))
        fd.write(Border + "\n")
        fd.write("--------Haribhau Automation Systems--------\n")
        fd.write("LogFile created at : "+str(timestamp) + "\n")
        fd.write("Total Files extension changed "+ str(iCount) + "\n")
        fd.write(Border + "\n")
        

    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) == 4:
        Script(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python script.py <DirectoryName> <extension1> <extension2>")
        print("Example: python script.py /home/user .txt .md")

if __name__ == "__main__":
    main()