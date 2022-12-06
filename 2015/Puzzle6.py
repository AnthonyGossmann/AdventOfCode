############################################################
# Import
############################################################
from Utils import *
from typing import List
import numpy as np
from enum import Enum
from itertools import product

############################################################
# Class Action
############################################################
class Action(Enum):
    TURN_OFF = 1
    TURN_ON = 2
    TOGGLE = 3
    
Action = Enum('Action', ['TURN_OFF', 'TURN_ON', 'TOGGLE'])

############################################################
# Class Puzzle6
############################################################
class Puzzle6:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.lights = np.zeros((1000, 1000))
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def applyInstructions1(self, ins_: List):
        for i,j in product(range(ins_[1], ins_[3]+1), range(ins_[2], ins_[4]+1)):
            if (ins_[0] == Action.TURN_OFF):
                self.lights[i][j] = 0
            elif (ins_[0] == Action.TURN_ON):
                self.lights[i][j] = 1
            else:
                self.lights[i][j] = not self.lights[i][j]
                
    def applyInstructions2(self, ins_: List):
        for i,j in product(range(ins_[1], ins_[3]+1), range(ins_[2], ins_[4]+1)):
            if (ins_[0] == Action.TURN_OFF):
                self.lights[i][j] = max(0, self.lights[i][j] - 1)
            elif (ins_[0] == Action.TURN_ON):
                self.lights[i][j] += 1
            else:
                self.lights[i][j] += 2

    def run(self):
        text = readFile(self.filename).replace("turn on", "turn_on").replace("turn off", "turn_off")
        
        instructions = []
        for line in re.split("\n", text):
            found = re.fullmatch("(.+) (.+),(.+) through (.+),(.+)", line)
            ins = []
            if (found.group(1) == "turn_off"):
                ins.append(Action.TURN_OFF)
            elif (found.group(1) == "turn_on"):
                ins.append(Action.TURN_ON)
            else:
                ins.append(Action.TOGGLE)
            
            for i in range(2, 6):
                ins.append(int(found.group(i)))
            instructions.append(ins)
            
        # Part 1
        for ins in instructions:
            self.applyInstructions1(ins)          
        self.result1 = int(self.lights.sum())
        
        # Part 2
        self.lights = np.zeros((1000, 1000))
        for ins in instructions:
            self.applyInstructions2(ins)          
        self.result2 = int(self.lights.sum())
    
        return            
