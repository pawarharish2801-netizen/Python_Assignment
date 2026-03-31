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
    ret = os.path.exists(DirectoryName)

    if ret == False:
        print("There is no such directory")
        return None
    
    ret = os.path.isdir(DirectoryName)

    if ret == False:
        print("The path is not a directory")
        return None
    
    Duplicate = {}
    
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

def WriteDuplicatesToLog(DirectoryName):
    """Find duplicates and write to Log.txt"""
    Border = "-" * 70
    
    print("Scanning directory for duplicate files...")
    
    MyDict = FindDuplicate(DirectoryName)
    
    if MyDict is None:
        return

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
    
    
    LogFileName = "Log.txt"
    timestamp = time.ctime()
    
    log_fd = open(LogFileName, 'w')
    
    log_fd.write(Border + "\n")
    log_fd.write("        Duplicate File Finder\n")
    log_fd.write(Border + "\n\n")
    log_fd.write(f"Directory Scanned: {DirectoryName}\n")
    log_fd.write(f"Log Created At: {timestamp}\n")
    log_fd.write(f"Total Duplicate Sets: {len(Result)}\n\n")
    log_fd.write(Border + "\n")
    
    if len(Result) == 0:
        log_fd.write("No duplicate files found\n")
        print("No duplicate files found")
    else:
        log_fd.write("Duplicate Files:\n")
        log_fd.write(Border + "\n\n")
        
        SetNumber = 1
        TotalDuplicates = 0
        
        for value in Result:
            log_fd.write(f"Duplicate Set {SetNumber}:\n")
            Count = 0
            
            for FilePath in value:
                log_fd.write(f"  {FilePath}\n")
                print(FilePath)
                Count += 1
            
            log_fd.write(f"  (Total: {Count} files)\n\n")
            TotalDuplicates += Count
            SetNumber += 1
        
        log_fd.write(Border + "\n")
        log_fd.write(f"Total duplicate files found: {TotalDuplicates}\n")
        
        print(f"\nTotal duplicate files found: {TotalDuplicates}")
    
    log_fd.write(Border + "\n")
    log_fd.close()
    
    print(f"\nLog file created: {os.path.abspath(LogFileName)}")

def main():
    if len(sys.argv) == 2:
        WriteDuplicatesToLog(sys.argv[1])
    else:
        print("Usage: python DirectoryDuplicate.py <DirectoryName>")
        print("Example: python DirectoryDuplicate.py Demo")

if __name__ == "__main__":
    main()
