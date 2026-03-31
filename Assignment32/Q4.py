import hashlib
import os
import sys
import time

def CalculateCheckSum(FileName):
    """Calculate MD5 checksum of a file"""
    try:
        fobj = open(FileName, "rb")
        
        hobj = hashlib.md5()

        Buffer = fobj.read(4096)

        while len(Buffer) > 0:
            hobj.update(Buffer) 
            Buffer = fobj.read(4096)
        
        fobj.close()

        return hobj.hexdigest()
    
    except Exception as e:
        print(f"Error reading {FileName}: {e}")
        return None

def FindDuplicate(DirectoryName):
    """Find duplicate files in a directory"""
    if not os.path.exists(DirectoryName):
        print("Error: Directory does not exist")
        return None
    
    if not os.path.isdir(DirectoryName):
        print("Error: Path is not a directory")
        return None
    
    Duplicate = {}
    
    print("Scanning directory for duplicate files...")
    
    for FolderName, SubfolderName, FileName in os.walk(DirectoryName):
        for FName in FileName:
            FilePath = os.path.join(FolderName, FName)
            
            if not os.path.isfile(FilePath):
                continue
            
            CheckSum = CalculateCheckSum(FilePath)
            
            if CheckSum is None:
                continue
            
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(FilePath)
            else:
                Duplicate[CheckSum] = [FilePath]
    
    return Duplicate

def DeleteDuplicates(DirectoryName):
    """Delete duplicate files and write to log"""
    Border = "-" * 70
    
    # Start timer
    StartTime = time.time()
    
    MyDict = FindDuplicate(DirectoryName)
    
    if MyDict is None:
        return
    
    # Filter only duplicates
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
    
    # Create log file
    LogFileName = "Log.txt"
    timestamp = time.ctime()
    
    log_fd = open(LogFileName, 'w')
    
    log_fd.write(Border + "\n")
    log_fd.write("        Duplicate File Removal Report\n")
    log_fd.write(Border + "\n\n")
    log_fd.write(f"Directory Scanned: {DirectoryName}\n")
    log_fd.write(f"Log Created At: {timestamp}\n\n")
    
    if len(Result) == 0:
        log_fd.write("No duplicate files found\n")
        print("\nNo duplicate files found")
    else:
        log_fd.write(Border + "\n")
        log_fd.write("Deleted Duplicate Files:\n")
        log_fd.write(Border + "\n\n")
        
        DeletedCount = 0
        SetNumber = 1
        
        for value in Result:
            log_fd.write(f"\nDuplicate Set {SetNumber}:\n")
            log_fd.write(f"Original File (Kept): {value[0]}\n")
            log_fd.write("Duplicates Deleted:\n")
            
            print(f"\nDuplicate Set {SetNumber}:")
            print(f"Original File (Kept): {value[0]}")
            print("Duplicates Deleted:")
            
            # Keep first file, delete rest
            for i in range(1, len(value)):
                FilePath = value[i]
                try:
                    os.remove(FilePath)
                    log_fd.write(f"  - {FilePath}\n")
                    print(f"  - {FilePath}")
                    DeletedCount += 1
                except Exception as e:
                    log_fd.write(f"  - ERROR deleting {FilePath}: {e}\n")
                    print(f"  - ERROR deleting {FilePath}: {e}")
            
            SetNumber += 1
        
        log_fd.write(f"\n{Border}\n")
        log_fd.write(f"Total duplicate files deleted: {DeletedCount}\n")
        log_fd.write(f"Total duplicate sets found: {len(Result)}\n")
        
        print(f"\n{Border}")
        print(f"Total duplicate files deleted: {DeletedCount}")
    
    # End timer
    EndTime = time.time()
    ExecutionTime = EndTime - StartTime
    
    log_fd.write(f"Execution Time: {ExecutionTime:.4f} seconds\n")
    log_fd.write(Border + "\n")
    log_fd.close()
    
    print(f"\nExecution Time: {ExecutionTime:.4f} seconds")
    print(f"Log file created: {os.path.abspath(LogFileName)}")

def main():
    print(Border := "-" * 70)
    print("        Duplicate File Removal Tool")
    print(Border)
    
    if len(sys.argv) == 2:
        DeleteDuplicates(sys.argv[1])
    else:
        print("\nUsage: python DirectoryDuplicateRemoval.py <DirectoryName>")
        print("Example: python DirectoryDuplicateRemoval.py Demo")

if __name__ == "__main__":
    main()
