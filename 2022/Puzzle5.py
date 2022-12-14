############################################################
# IMPORT
############################################################
from Utils import *
import typing
from typing import Dict
from typing import List
import re

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["05.txt", "05.ex"]

############################################################
# METHODS
############################################################

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: str
    reuslt2: str
    stacks: Dict[int,List[str]]
    commands: List[List[int]]
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = ""
        self.result2 = ""
        self.stacks = {}
        self.commands = []
    
    def getResult1(self) -> str:
        return self.result1

    def getResult2(self) -> str:
        return self.result2
    
    def loadStacks(self):
        text = readFile(self.filename)
        lines = text.split("\n")
        
        self.stacks = {}
        self.commands = []
        
        for line in lines:
            if ('[' in line):
                # Load Stacks
                line = re.sub("[\[\]]", "", line)
                tokens = re.split("[\s]{4}", line)
                
                crates = []
                for token in tokens:
                    crates += re.split(" ", token)
                
                for i in range(len(crates)):
                    if (i+1) not in self.stacks.keys():
                        self.stacks[i+1] = []
                    if (crates[i] != ''):
                        self.stacks[i+1].insert(0, crates[i])
                        
            elif ("move" in line):
                # Load commands
                found =  re.fullmatch("move (.+) from (.+) to (.+)", line)
                self.commands.append([int(found.group(2)), int(found.group(3)), int(found.group(1))])
    
    def move(self, crateMover9001_: bool = False) -> str:
        for cmd in self.commands:     
            if crateMover9001_:
                    items = self.stacks[cmd[0]][-cmd[2]:]
                    self.stacks[cmd[0]] = self.stacks[cmd[0]][:-cmd[2]]
                    self.stacks[cmd[1]] += items
            else:
                for i in range(cmd[2]):
                    item = self.stacks[cmd[0]][-1]
                    self.stacks[cmd[0]] = self.stacks[cmd[0]][:-1]
                    self.stacks[cmd[1]].append(item)
                    
        result = ""
        for stack in self.stacks.values():
            if (len(stack) != 0):
                result += stack[-1]
                
        return result

    def run(self):
        # Part 1
        self.loadStacks()
        self.result1 = self.move()
        
        # Part 2
        self.loadStacks()
        self.result2 = self.move(True)

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))
