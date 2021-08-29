def removeLine(myFileObj,lines,lineNumber):
    myFileObj.seek(lineNumber-1)
    myFileObj.writelines(lines[lineNumber:])