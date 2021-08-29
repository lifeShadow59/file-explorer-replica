import io


def openFile(filePath:str,fileOpenType:str) -> io.TextIOWrapper:
    
    return open(filePath, fileOpenType)
