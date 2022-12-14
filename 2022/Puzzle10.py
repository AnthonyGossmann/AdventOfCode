############################################################
# IMPORT
############################################################
from Utils import *
import re

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["10.txt", "10a.ex", "10b.ex"]

############################################################
# METHODS
############################################################
def execute(cmds_: List, cycle_: int, x_: int) -> int:
    for cmd in cmds_:
        if (cmd[0] == cycle_):
            x_ += cmd[1]
    return x_

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: str
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = '\n'
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> str:
        return self.result2
    
    def loadCmds(self) -> List:
        lines = readLines(self.filename)
        cycle = 0
        cmds = []
        
        for line in lines:
            if ("noop" in line):
                cycle += 1
            elif ("addx" in line):
                cycle += 2
                value = int(re.split(" ", line)[-1])
                cmds.append([cycle + 1, value])
                
        return cmds

    def run(self):
        cmds = self.loadCmds()
        
        cycle = 0
        x = 1
        width = 40
        for i in range(240):
            cycle += 1
            x = execute(cmds, cycle, x)
            
            if ((cycle % 40) == 20):
                self.result1 += cycle * x
                
            col = (cycle - 1) % width
            if (x in [col-1, col, col+1]):
                self.result2 += '#'
            else:
                self.result2 += '.'
            
            if (col == (width - 1)):
                self.result2 += '\n'
                 
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))