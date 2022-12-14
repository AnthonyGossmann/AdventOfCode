############################################################
# IMPORT
############################################################
from Utils import *
import typing
from typing import List
from typing import Tuple

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["03.txt", "03.ex"]
    
############################################################
# METHODS
############################################################
    
############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
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
    
    def track(self, start_: int = 0, step_: int = 1) -> List:
        cmds = readFile(self.filename)
        
        houses = [(0,0)]
        x = 0
        y = 0
        
        for i in range(start_, len(cmds), step_):
            if (cmds[i] == "v"):
                y -= 1
            elif (cmds[i] == "^"):
                y += 1
            elif (cmds[i] == "<"):
                x -= 1
            else:
                x += 1

            house = (x,y)
            if house not in houses:
                houses.append(house)

        return houses

    def run(self):
        # Part 1
        houses = self.track()
        self.result1 = len(houses)
        
        # Part 2
        houses = self.track(0, 2) + self.track(1, 2)
        houses = [houses[i] for i in range(len(houses)) if i == houses.index(houses[i]) ]
        self.result2 = len(houses)
        
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))              
