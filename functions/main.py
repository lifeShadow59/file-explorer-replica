import io
import os
import remove_line as removeLine
from open_file import openFile
from const.const_string import ConstantString 
from get_ascii_value import getAsciiValue
from typing import Tuple


def getFileOrDirName(line:str) -> Tuple[str,bool]:
    indexOfInvertedComma:int = 1
    fileOrDirName = ''
    for i in range(0,len(line)):
        if line[i] == '"':
            if indexOfInvertedComma == 3:
                break
            indexOfInvertedComma = indexOfInvertedComma + 1
        if indexOfInvertedComma == 2:

            fileOrDirName = fileOrDirName + ('' if line[i] == '"'  else line[i])
    isDirectoryAvailable:bool = False 
    if (line.find('directory') == -1):
        isDirectoryAvailable = False
    else:
        isDirectoryAvailable = True
    return fileOrDirName , isDirectoryAvailable


myFile:io.TextIOWrapper = openFile(ConstantString.SOURCE_FILES_PATH,ConstantString.FILE_OPEN_IN_READ_AND_WRITE_MODE)
lines =  myFile.readlines()


PATH:str = os.path.dirname(os.path.realpath(__file__))

current_path:str =PATH
pastPathList:str = [PATH]

for i in range(2,len(lines) - 5):
    dirName , isDirectoryAvailable = getFileOrDirName(lines[i])
    if dirName == '' and isDirectoryAvailable:
        pastPathList.pop()
        current_path = pastPathList[-1]

    elif isDirectoryAvailable:        
        if not dirName == '.':
            current_path = os.path.join(current_path,dirName)
        else:
            current_path = os.path.join(current_path,'mains')
        os.mkdir(current_path)
        pastPathList.append(current_path)
    
    else :
        with open(os.path.join(current_path, dirName), 'w') as fp:
            pass

myFile.close()