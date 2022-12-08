############################################################
# Import
############################################################
from Utils import *

############################################################
# Static Methods
############################################################
def findNextClosingBrace(text_: str, pos_: int) -> int:
    found = 1
    for i, c in enumerate(text_[pos_:], start = pos_):
        if (c == "{"):
            found += 1
        elif (c == "}"):
            found -= 1
        if (found == 0):
            return i
    return -1

############################################################
# Class Puzzle12
############################################################
class Puzzle12:
    filename: str
    result1: int
    result2: int
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        text = readFile(self.filename)        

        # Part 1
        tokens = apply(int, re.findall("-?\d+", text))    
        self.result1 = sum(tokens)
        
        # Part 2
        buffer = []
        i = 0
        while (i < len(text)):
            c = text[i]
            if (c == "{"):
                buffer.append(i)
            elif (c == "}"):
                buffer.pop()
            if ((c == ":") and buffer and (text[i:(i+6)] == ':"red"')):
                first = buffer[-1]
                close = findNextClosingBrace(text, i)
                text = text[:first] + text[(close + 1):]
                i = 0
                buffer.clear()
            else:
                i += 1
        
        tokens =  apply(int, re.findall("-?\d+", text))   
        self.result2 = sum(tokens)
        
        return            
