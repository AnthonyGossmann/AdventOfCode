############################################################
# Import
############################################################
from Utils import *
from typing import List
from itertools import product

############################################################
# Static Methods
############################################################
def buildKey(x_: int, y_: int) -> str:
    return '(' + str(x_) + ',' + str(y_) + ')'

############################################################
# Class Light
############################################################
class Light:
    def __init__(self, x_: int, y_: int, state_: bool, gridSize_: int):
        self.key = buildKey(x_, y_)
        self.x = x_
        self.y = y_
        self.state = state_
        self.neighbour = self.getNeighbours(gridSize_)
        
    def getNeighbours(self, gridSize_: int) -> List:
        ngh = []
        x = [self.x - 1, self.x, self.x + 1]
        y = [self.y - 1, self.y, self.y + 1]
        
        x = [x[i] for i in range(len(x)) if ((x[i] != -1) and (x[i] != gridSize_))]
        y = [y[i] for i in range(len(y)) if ((y[i] != -1) and (y[i] != gridSize_))]

        for i,j in product(x,y):
            if ((i != self.x) or (j != self.y)):
                ngh.append(buildKey(i, j))
        
        return ngh
    
    def updateState(self, lights_: List) -> bool: 
        ctr = 0
        for ngh in self.neighbour:
            if (lights_[ngh].state):
                ctr += 1
                
        state = self.state
        
        if (self.state):
            if ((ctr != 2) and (ctr != 3)):
                state = False
        elif not self.state:
            if (ctr == 3):
                state = True
            
        return state
                
############################################################
# Class Puzzle18
############################################################
class Puzzle18:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadLights(self, lines_: List[str], gridSize_: int) -> List:
        lights = {}
        for i in range(gridSize_):
            for j in range(gridSize_):
                key = buildKey(i, j)
                if (lines_[i][j] == '#'):
                    lights[key] = Light(i, j, True, gridSize_)
                else:
                    lights[key] = Light(i, j, False, gridSize_)
        return lights
    
    def process(self, lights_: List, gridSize_: int, step_: int, stuck_: bool = False) -> int:
        count = 0
        states = {}
        results = lights_.copy()
        for i in range(step_):
            for light in results.values():
                states[light.key] = light.updateState(results)
            for key in states.keys():
                if (stuck_ and ((key == buildKey(0,0)) or (key == buildKey(0,gridSize_-1)) or (key == buildKey(gridSize_-1,0)) or (key == buildKey(gridSize_-1,gridSize_-1)))):
                    continue
                results[key].state = states[key]
                
        for light in results.values():
            if light.state:
                count += 1
                
        return count
            
    
    def run(self):
        step = 100
        
        lines = readLines(self.filename)
        gridSize = len(lines)

        # Part 1
        lights = self.loadLights(lines, gridSize)
        self.result1 = self.process(lights, gridSize, step)
                
        # Part 2
        lights = self.loadLights(lines, gridSize)
        lights[buildKey(0,0)].state = True
        lights[buildKey(0,gridSize-1)].state = True
        lights[buildKey(gridSize-1,0)].state = True
        lights[buildKey(gridSize-1,gridSize-1)].state = True
        self.result2 = self.process(lights, gridSize, step, True)
    
        return            
