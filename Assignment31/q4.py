import os 
import sys
import time

def Script(Dsource, Ddest , Ext):
    iCount = 0 
    Border = "-"*60
    FileCount = 0 

    try:
        if not os.path.isdir(Dsource):
            print("Error: The path mentioned is not a directory")
            return
        
        timestamp = time.ctime()
        LogFileName = "Q4%s.log" % (timestamp)
        LogFileName = LogFileName.replace(" ", "_")
        LogFileName = LogFileName.replace(":", "_")

        filelist = os.listdir(Dsource)

        if len(filelist) == 0:
            print("No file in the source Directory")
        
        filtered_files = list(filter(lambda file  : file.endswith(Ext),filelist ))
        
        os.mkdir(Ddest)

        for file in filtered_files:
            fSourcepath = os.path.join(Dsource,file)
            
            fSource = open(fSourcepath,'r')
            Data = fSource.read()

            fNewPath = os.path.join(Ddest,file)

            fDest = open(fNewPath,'w')
            fDest.write(Data)
            iCount +=1 
 
        # Write log file
        log_fd =open(LogFileName, 'w') 
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
    if len(sys.argv) == 4:
        Script(sys.argv[1], sys.argv[2] ,sys.argv[3])
    else:
        print("Usage: python filename <DirectorySource> <DirectoryDest> <ext>")
        print("Example: python filename Demo Marvellous .txt")

if __name__ == "__main__":
    main()