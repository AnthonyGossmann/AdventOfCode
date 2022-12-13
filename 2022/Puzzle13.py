############################################################
# Import
############################################################
from Utils import *
from typing import List
from typing import Dict
import re
import functools

############################################################
# Methods
############################################################
def getNextClosingBrackets(text_: str, start_: int):
    counter = 0
    for i in range(start_, len(text_)):
        if (text_[i] == '['):
            counter += 1
        elif (text_[i] == ']'):
            counter -= 1
            if (counter == 0):
                return i
    raise Exception("Closing bracket not found.")

def splitOutsideBrackets(text_: str):
    tokens = []
    counter = 0
    last = 0
    
    for i in range(len(text_)):
        if (text_[i] == '['):
            counter += 1
        elif (text_[i] == ']'):
            counter -= 1
        
        if ((text_[i] == ',') and (counter == 0)):
            tokens.append(text_[last:i])
            last = i+1
    tokens.append(text_[last:])
    
    return tokens
    
def getItems(text_: str):
    text = text_
    if text.startswith('['):
        close = getNextClosingBrackets(text, 0)
        text = text[1:close]
    
    items = splitOutsideBrackets(text)
    
    return items

def compare(l1_: str, l2_: str) -> int:
    #print("Compare " + l1_ + " vs " + l2_)
    
    # Empty items
    if (l1_ == "[]") and (l2_ == "[]"):
        return 0
    elif (l1_ == "[]"):
        return 1
    elif (l2_ == "[]"):
        return -1
    
    # Mixed types
    if (l1_.startswith('[') and not l2_.startswith('[')):
        l2_ = '[' + l2_ + ']'
    if (l2_.startswith('[') and not l1_.startswith('[')):
        l1_ = '[' + l1_ + ']'
        
    # Compare items
    if (('[' not in l1_) and ('[' not in l2_)):
        if (int(l1_) == int(l2_)):
            return 0
        elif (int(l1_) < int(l2_)):
            return 1
        else:
            return -1

    # Children
    i1 = getItems(l1_)
    i2 = getItems(l2_)
    
    for i in range(min(len(i1), len(i2))):
        res = compare(i1[i], i2[i])
        if (res != 0):
            return res
    
    # Ran out of items
    if (len(i1) < len(i2)):
        return 1
    elif (len(i1) > len(i2)):
        return -1

    return 0

############################################################
# Class Puzzle13
############################################################
class Puzzle13:
    filename: str
    result1: int
    result2: int
    
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        lines = readLines(self.filename)
        lines = [line for line in lines if len(line) != 0]
        
        # Part 1
        for i in range(0, len(lines)-1, 2):
            res = compare(lines[i], lines[i+1])
            if (res == 1):
                self.result1 += (i // 2) + 1
    
        # Part 2
        lines.append("[[2]]")
        lines.append("[[6]]")
        
        sorted_lines = sorted(lines, key=functools.cmp_to_key(compare))
        sorted_lines = sorted_lines[::-1]
        
        self.result2 = (sorted_lines.index("[[2]]") + 1) * (sorted_lines.index("[[6]]") + 1)
            
        
        return            
