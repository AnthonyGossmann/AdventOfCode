############################################################
# Import
############################################################
from Utils import *
from typing import List

############################################################
# Static Methods
############################################################
def track(cmds: str, start: int = 0, step: int = 1) -> List[List[int]]:
    houses = [[0,0]]
    x = 0
    y = 0
    
    for i in range(start, len(cmds), step):
        if (cmds[i] == "v"):
            y -= 1
        elif (cmds[i] == '^'):
            y += 1
        elif (cmds[i] == '<'):
            x -= 1
        else:
            x += 1
        
        if ([x,y] not in houses):
            houses.append([x,y])
    return houses

############################################################
# Class Puzzle3
############################################################
class Puzzle3:
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
        houses = track(text)
        self.result1 = len(houses)
        
        # Part 2
        houses = track(text, 0, 2) + track(text, 1, 2)
        houses = [i for n, i in enumerate(houses) if i not in houses[:n]]     
        self.result2 = len(houses)
        
    
        return            
