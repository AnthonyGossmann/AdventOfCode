############################################################
# IMPORT
############################################################
from Utils import *
import numpy as np
from enum import Enum
from itertools import product
import typing
from typing import List
from typing import NewType
from dataclasses import dataclass

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["06.txt", "06.ex"]

############################################################
# CLASS ACTION
############################################################
class Action(Enum):
    TURN_OFF = 1
    TURN_ON = 2
    TOGGLE = 3
    
Action = Enum('Action', ['TURN_OFF', 'TURN_ON', 'TOGGLE'])

############################################################
# CLASS COMMAND
############################################################
Command = typing.NewType("Command", None)
@dataclass()
class Command:
    action = Action
    x1: int
    y1: int
    x2: int
    y2: int
    
    def __init__(self, action_: Action, x1_: int, y1_: int, x2_: int, y2_: int):
        self.action = action_
        self.x1 = x1_
        self.y1 = y1_
        self.x2 = x2_
        self.y2 = y2_
        
    def apply(self, lights_: np.array, elvish_: bool = False):
        for x,y in product(range(self.x1, self.x2 + 1), range(self.y1, self.y2 + 1)):
            if (self.action == Action.TURN_OFF):
                if elvish_:
                    lights_[x][y] = max(0, lights_[x][y] - 1)
                else:
                    lights_[x][y] = 0
            elif (self.action == Action.TURN_ON):
                if elvish_:
                    lights_[x][y] += 1
                else:
                    lights_[x][y] = 1
            else:
                if elvish_:
                    lights_[x][y] += 2
                else:
                    lights_[x][y] = not lights_[x][y]

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    lights: np.array
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.lights = np.zeros((1000, 1000))
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        text = readFile(self.filename).replace("turn on", "turn_on").replace("turn off", "turn_off")
        
        cmds = []
        for line in re.split("\n", text):
            found = re.fullmatch("(.+) (.+),(.+) through (.+),(.+)", line)
            if (found.group(1) == "turn_off"):
                cmd = Command(Action.TURN_OFF, int(found.group(2)), int(found.group(3)), int(found.group(4)), int(found.group(5)))          
            elif (found.group(1) == "turn_on"):
                cmd = Command(Action.TURN_ON, int(found.group(2)), int(found.group(3)), int(found.group(4)), int(found.group(5)))
            else:
                cmd = Command(Action.TOGGLE, int(found.group(2)), int(found.group(3)), int(found.group(4)), int(found.group(5)))
            cmds.append(cmd)
            
        # Part 1
        for cmd in cmds:
            cmd.apply(self.lights)        
        self.result1 = int(self.lights.sum())
        
        # Part 2
        self.lights = np.zeros((1000, 1000))
        for cmd in cmds:
            cmd.apply(self.lights, True)           
        self.result2 = int(self.lights.sum())
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))           
