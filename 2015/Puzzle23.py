############################################################
# IMPORT
############################################################
from Utils import *
import typing
from typing import List

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["23.txt", "23.ex"]

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    a: int
    b: int
    cmds: List
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.a = 0
        self.b = 0
        self.cmds = []
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadCmd(self):
        lines = readLines(self.filename)
        
        for line in lines:
            tokens = list(filter(None, re.split("[ ,]", line)))
            self.cmds.append(tokens)
            
    def apply(self):
        i = 0
        while (i < len(self.cmds)):
            cmd = self.cmds[i]
            
            if (cmd[0] == "inc"):
                if (cmd[1] == 'a'):
                    self.a += 1
                else:
                    self.b += 1
            elif (cmd[0] == "tpl"):
                if (cmd[1] == 'a'):
                    self.a *= 3
                else:
                    self.b *= 3
            elif (cmd[0] == "hlf"):
                if (cmd[1] == 'a'):
                    self.a = self.a // 2
                else:
                    self.b = self.b // 2
            elif (cmd[0] == "jmp"):
                i += int(cmd[1])
                continue
            elif (cmd[0] == "jie"):
                if (cmd[1] == 'a'):
                    if ((self.a % 2) == 0):
                        i += int(cmd[2])
                        continue
                else:
                    if ((self.b % 2) == 0):
                        i += int(cmd[2])
                        continue
            else:
                if (cmd[1] == 'a'):
                    if (self.a == 1):
                        i += int(cmd[2])
                        continue
                else:
                    if (self.b == 1):
                        i += int(cmd[2])
                        continue
                    
            i += 1

    def run(self):
        self.loadCmd()
        
        # Part 1
        self.apply()
        self.result1 = self.b
        
        # Part 2
        self.a = 1
        self.b = 0
        self.apply()
        self.result2 = self.b
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))           
