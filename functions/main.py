import io
import os
import remove_line as removeLine
from open_file import openFile
from  const.const_string import ConstantString 
from get_ascii_value import getAsciiValue

indexValue:int = 4


myFile:io.TextIOWrapper = openFile(ConstantString.SOURCE_DIRS_PATH,ConstantString.FILE_OPEN_IN_READ_AND_WRITE_MODE)
lines =  myFile.readlines()

# for line in lines:
#     x = line[indexValue:]
#     print(x,end='')
PATH:str = os.path.dirname(os.path.realpath(__file__))
print(ord('│'))

# This is For get Files and folder list
# for i in range(1,len(lines) - 2):
#     # dir
#     print(i+1 , '    ' ,lines[i][indexValue:],end='')
#     # path = os.path.join(PATH, lines[i][indexValue:][:-1])
#     # os.mkdir(path)



    

#     try:
#         asciiValue = getAsciiValue(lines[i+1][indexValue])
#         i-1
#         if asciiValue == 9500 or asciiValue == 9492 or asciiValue == 9474:
#             indexValue = indexValue + 4

#         xasciiValue = getAsciiValue(lines[i+1][indexValue-4])
#         i-1
#         if (xasciiValue == 9500 or xasciiValue == 9492 or xasciiValue == 9474):
#             pass

#         else:
#             indexValue = indexValue - 4
#     except IndexError:
#         print('index not in range')












myFile.close()
# removeLine(my_file,lines,1)
# x = lines[1][indexValue:]
# print(x,end='')