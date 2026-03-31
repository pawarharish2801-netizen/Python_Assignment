import hashlib
import os

def CalculateCheckSum(FileName):

    fobj = open(FileName , "rb")
    
    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) >0):
            hobj.update(Buffer) 
            Buffer = fobj.read(1000)
        
    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
    ret = False 

    ret = os.path.exists(DirectoryName)

    if (ret == False):
        print("There is no Such Directory ")
        return 
    
    ret = os.path.isdir(DirectoryName)

    if (ret == False):
        print("There is no such Directory ")
        return 
    
    Duplicate = {}
    for FolderName ,Subfoldername , FileName in os.walk(DirectoryName):
        
        for FName in FileName:
            FName = os.path.join(FolderName,FName)
            CheckSum = CalculateCheckSum(os.path.join(FName))

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(FName)
            else:
                Duplicate[CheckSum] = [FName]
    
    return Duplicate

def DisplayResult(MyDict):

    Result = list(filter(lambda x : len(x) > 1 , MyDict.values() ))

    Count = 0 

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("Value of Count is : ",Count)
        Count = 0

def DeleteDuplicate(path = "Marvellous"):
    mydict = FindDuplicate(path)

    Result = list(filter(lambda x : len(x) > 1 , mydict.values() ))

    Count = 0 
    Cnt = 0 

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if (Count > 1):
                print("Delete file : ",subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0 
    print("Total Deleted Files ",Cnt)


        
def main():
     
    DeleteDuplicate()

if __name__ == "__main__":
    main()