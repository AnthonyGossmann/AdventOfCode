############################################################
# IMPORT
############################################################
from Utils import *
import copy
from itertools import product
import typing
from typing import Dict
from typing import List

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["09.txt", "09.ex"]

############################################################
# METHODS
############################################################
def neighbours(pos_: List) -> List:
    x = [i for i in range(pos_[0]-1,pos_[0]+2)]
    y = [i for i in range(pos_[1]-1,pos_[1]+2)]
        
    ngh = []
    for i,j in product(x,y):
        ngh.append([i,j])
        
    return ngh

def move(rope_: List, cmd_: str):
    if (cmd_ == 'D'):
        rope_[0][1] -= 1
    elif (cmd_ == 'U'):
        rope_[0][1] += 1
    elif (cmd_ == 'L'):
        rope_[0][0] -= 1
    else:
        rope_[0][0] += 1

    for i in range(1, len(rope_)):
        if (rope_[i] not in neighbours(rope_[i-1])):
            dx = (rope_[i-1][0] - rope_[i][0])
            dy = (rope_[i-1][1] - rope_[i][1])
            
            if (dx < -1):
                dx = -1
            elif (dx > 1):
                dx = 1
            
            if (dy < -1):
                dy = -1
            elif (dy > 1):
                dy = 1
                
            rope_[i][0] += dx
            rope_[i][1] += dy

    return rope_

def execute(cmds_: List, length_: int) -> int:
    checked = [[0,0]]
    rope = [[0,0] for i in range(length_)]

    for cmd in cmds_:
        for i in range(cmd[1]):
            rope = move(rope, cmd[0])
            if rope[-1] not in checked:
                checked.append(copy.copy(rope[-1]))

    return len(checked)

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

    def run(self):
        lines = readLines(self.filename)
        
        commands = []
        for line in lines:
            tokens = line.split(" ")
            commands.append([tokens[0], int(tokens[1])])

        self.result1 = execute(commands, 2)
        self.result2 = execute(commands, 10)

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))
