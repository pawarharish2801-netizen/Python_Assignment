import os 
import sys
import time

def Script(Dsource, Ddest):
    iCount = 0 
    Border = "-"*60
    FileCount = 0 

    try:
        if not os.path.isdir(Dsource):
            print("Error: The path mentioned is not a directory")
            return
        
        timestamp = time.ctime()
        LogFileName = "Q3%s.log" % (timestamp)
        LogFileName = LogFileName.replace(" ", "_")
        LogFileName = LogFileName.replace(":", "_")

        filelist = os.listdir(Dsource)

        if len(filelist) == 0:
            print("No file in the source Directory")
        else:

            if not os.path.exists(Ddest):
                os.mkdir(Ddest)
            
            for FolderName, SubFolder, Filename in os.walk(Dsource):
                for FName in Filename:
                    
                    fSourcePath = os.path.join(FolderName, FName)
                    
                    with open(fSourcePath, "r") as fSource:
                        Data = fSource.read()
                    
                    fNewName = os.path.join(Ddest, FName)
                    print(fNewName)
                    
                    with open(fNewName, "w") as fDest:
                        fDest.write(Data)
                    
                    FileCount += 1
                    iCount += 1
        
        with open(LogFileName, 'w') as log_fd:
            print("Log Report Generated at: " + os.path.abspath(LogFileName))
            log_fd.write(Border + "\n")
            log_fd.write("--------Haribhau Automation Systems--------\n")
            log_fd.write("LogFile created at: " + str(timestamp) + "\n")
            log_fd.write("Total Files copied: " + str(iCount) + "\n")
            log_fd.write(Border + "\n")

    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) == 3:
        Script(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python filename <DirectorySource> <DirectoryDest>")
        print("Example: python filename Demo Marvellous")

if __name__ == "__main__":
    main()