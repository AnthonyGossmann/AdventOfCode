############################################################
# IMPORT
############################################################
from Utils import *
from itertools import product
import typing
from typing import List
from typing import Dict
from typing import Tuple
from typing import NewType
from dataclasses import dataclass

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["18.txt", "18.ex"]

############################################################
# METHODS
############################################################
    
############################################################
# CLASS LIGHT
############################################################
Light = typing.NewType("Light", None)
@dataclass()
class Light:
    pos: Tuple[int,int]
    state: bool
    size: int
    neighbours: List
    
    def __init__(self, pos_: Tuple[int,int], state_: bool, size_: int):
        self.pos = pos_
        self.state = state_
        self.size = size_
        self.neighbours = []
        
        x = [self.pos[0] - 1, self.pos[0], self.pos[0] + 1]
        y = [self.pos[1] - 1, self.pos[1], self.pos[1] + 1]
        
        x = [x[i] for i in range(len(x)) if ((x[i] != -1) and (x[i] != self.size))]
        y = [y[i] for i in range(len(y)) if ((y[i] != -1) and (y[i] != self.size))]
        
        for i,j in product(x,y):
            if ((i != self.pos[0]) or (j != self.pos[1])):
                self.neighbours.append((i,j))
                
    def update(self, lights_: Dict) -> bool:
        count = 0
        for ngh in self.neighbours:
            if (lights_[ngh].state):
                count += 1
        
        state = self.state
        if self.state:
            if ((count != 2) and (count != 3)):
                state = False
        else:
            if (count == 3):
                state = True
                
        return state    
                
############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    lights: Dict
    size: int
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.lights = {}
        self.size = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadLights(self):
        lines = readLines(self.filename)
        self.size = len(lines)
        
        self.lights = {}
        for i,j in product(range(self.size), range(self.size)):
            light = Light((i,j), (lines[i][j] == '#'), self.size)
            self.lights[(i,j)] = light
    
    def step(self, step_: int, stuck_: bool = False) -> int:
        count = 0
        states = {}
        results = self.lights.copy()
        
        for i in range(step_):
            for light in results.values():
                states[light.pos] = light.update(results)
     
            for pos in states.keys():
                if (stuck_ and ((pos == (0,0) or (pos == (0,self.size - 1)) or (pos == (self.size - 1,0)) or (pos == (self.size - 1,self.size - 1))))):
                    continue
                results[pos].state = states[pos]
                
        for light in results.values():
            if light.state:
                count += 1
                
        return count
            
    def run(self):
        step = 100

        # Part 1
        self.loadLights()
        self.result1 = self.step(step)
                
        # Part 2
        self.loadLights()
        self.lights[(0,0)].state = True
        self.lights[(0,self.size-1)].state = True
        self.lights[(self.size-1,0)].state = True
        self.lights[(self.size-1,self.size-1)].state = True
        self.result2 = self.step(step, True)
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))            
