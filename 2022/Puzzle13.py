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
def compare(l1_, l2_):
    for i in range(min(len(l1_), len(l2_))):
        if ((type(l1_[i]) == int) and (type(l2_[i]) == int)):
            if (l1_[i] == l2_[i]):
                continue
            return (l1_[i] - l2_[i])
        
        res = compare(l1_[i] if (type(l1_[i]) == list) else [l1_[i]], l2_[i] if (type(l2_[i]) == list) else [l2_[i]])
        if res:
            return res
    
    return (len(l1_) - len(l2_))

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
        lines = [eval(line) for line in lines if len(line) != 0]
        
        # Part 1
        for i in range(0, len(lines)-1, 2):
            res = compare(lines[i], lines[i+1])
            if (res < 0):
                self.result1 += (i // 2) + 1
    
        # Part 2
        lines.append(eval("[[2]]"))
        lines.append(eval("[[6]]"))
        
        sorted_lines = sorted(lines, key=functools.cmp_to_key(compare))
        self.result2 = (sorted_lines.index(eval("[[2]]")) + 1) * (sorted_lines.index(eval("[[6]]")) + 1)
            
        
        return            
