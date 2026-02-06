import os 
import sys
import time
import hashlib

def Script(Dsource):
    Border = "-" * 60
    file_info = []

    try:
        if not os.path.isdir(Dsource):
            print("Error: The path mentioned is not a directory")
            return
        
        timestamp = time.ctime()
        LogFileName = "Q4_%s.log" % (timestamp)
        LogFileName = LogFileName.replace(" ", "_")
        LogFileName = LogFileName.replace(":", "_")

        filelist = os.listdir(Dsource)

        print("Calculating checksums...\n")

        for file in filelist:
            file_path = os.path.join(Dsource, file)
            
            if not os.path.isfile(file_path):
                continue
            
            try:
                file_size = os.path.getsize(file_path)
                
                fobj = open(file_path, "rb")
                hobj = hashlib.md5()
                
                while True:
                    Buffer = fobj.read(4096)
                    if not Buffer:
                        break
                    hobj.update(Buffer)
                
                fobj.close()
                
                checksum = hobj.hexdigest()
                print(f"{file}: {checksum}")
                file_info.append((file, checksum, file_size))
            
            except Exception as e:
                print(f"Error processing {file}: {e}")
 

        log_fd = open(LogFileName, 'w')
        log_fd.write(Border + "\n")
        log_fd.write("        Haribhau Automation Systems\n")
        log_fd.write("        File Checksum Report\n")
        log_fd.write(Border + "\n\n")
        log_fd.write(f"Directory        : {Dsource}\n")
        log_fd.write(f"Log created at   : {timestamp}\n")
        log_fd.write(f"Total Files      : {len(file_info)}\n\n")
        log_fd.write(Border + "\n")
        log_fd.write(f"{'Filename':<30} {'MD5 Checksum':<35} {'Size (bytes)'}\n")
        log_fd.write(Border + "\n")
        
        for file, checksum, size in file_info:
            log_fd.write(f"{file:<30} {checksum:<35} {size}\n")
        
        log_fd.write(Border + "\n")
        log_fd.close()
        
        print(f"\nLog Report Generated at: {os.path.abspath(LogFileName)}")
        print(f"Total Files processed: {len(file_info)}")

    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) == 2:
        Script(sys.argv[1])
    else:
        print("Usage: python filename.py <DirName>")
        print("Example: python filename.py /home/user/documents")

if __name__ == "__main__":
    main()