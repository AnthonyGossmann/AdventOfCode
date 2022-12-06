############################################################
# Import
############################################################
from Utils import *
from typing import List
from itertools import product

############################################################
# Class Light
############################################################
class Light:
    def __init__(self, x_: int, y_: int, state_: bool):
        self.x = x_
        self.y = y_
        self.state = state_
        self.neighbour = self.getNeighbours()
        
    def getNeighbours(self) -> List:
        ngh = []
        x = [self.x - 1, self.x, self.x + 1]
        y = [self.y - 1, self.y, self.y + 1]
        
        x = [x[i] for i in range(len(x)) if ((x[i] != -1) and (x[i] != 100))]
        y = [y[i] for i in range(len(y)) if ((y[i] != -1) and (y[i] != 100))]

        for i,j in product(x,y):
            if ((i != self.x) or (j != self.y)):
                ngh.append([i, j])
        
        return ngh
    
    def getState(self, lights_: List, x_: int, y_: int) -> bool:
        for light in lights_:
            if ((light.x = x_) and (light.y == y_)):
                return light.State
        return False
    
    def update(self, lights_: List) -> List:
        ctr = 0
        for ngh in self.neighbour:
            if (getState(lights_, ngh[0], ngh[1]))
        

############################################################
# Class Puzzle18
############################################################
class Puzzle18:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.lights = []
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        lines = readLines(self.filename)
        
        for i in range(len(lines)):
            for j in range(lines[i]):
                if (lines[i][j] == '#'):
                    self.lights.append(Light(i, j, True))
                else:
                    self.lights.append(Light(i, j, False))

        # Part 1
  
    
        return            
