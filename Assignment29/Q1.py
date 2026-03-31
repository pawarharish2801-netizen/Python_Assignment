import os
def main():
    Fname = input("Write the name of file : ")

    fd = open(Fname , 'r')

    bRet = os.path.exists(Fname)

    if (bRet == True):
        print("File Opened Successfully")
        fd.close()

    else:
        print("File is not there")
        
    

if __name__ == "__main__":
    main()