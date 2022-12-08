############################################################
# Import
############################################################
from Utils import *
from itertools import product
import typing
from typing import List
from typing import Dict
from typing import NewType
from dataclasses import dataclass

Point = typing.NewType("Point", None)
Light = typing.NewType("Light", None)

############################################################
# Class Point
############################################################
@dataclass()
class Point:
    x: int
    y: int
    
    def __init__(self, x_: int, y_: int):
        self.x = x_
        self.y = y_
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other_):
        return (self.x, self.y) == (other_.x, other_.y)

    def __ne__(self, other_):
        return not(self == other_)
    
############################################################
# Class Light
############################################################
@dataclass()
class Light:
    point: Point
    state: bool
    size: int
    neighbours: List[Point]
    
    def __init__(self, point_: Point, state_: bool, size_: int):
        self.point = point_
        self.state = state_
        self.size = size_
        self.neighbours = []
        
        x = [self.point.x - 1, self.point.x, self.point.x + 1]
        y = [self.point.y - 1, self.point.y, self.point.y + 1]
        
        x = [x[i] for i in range(len(x)) if ((x[i] != -1) and (x[i] != self.size))]
        y = [y[i] for i in range(len(y)) if ((y[i] != -1) and (y[i] != self.size))]
        
        for i,j in product(x,y):
            if ((i != self.point.x) or (j != self.point.y)):
                self.neighbours.append(Point(i,j))
                
    def update(self, lights_: Dict[Point, Light]) -> bool:
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
# Class Puzzle18
############################################################
class Puzzle18:
    filename: str
    result1: int
    result2: int
    lights: Dict[Point,Light]
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
    
    def loadLights(self, lines_: List[str]) -> Dict[Point, Light]:
        lights = dict()
        for i,j in product(range(self.size), range(self.size)):
            light = Light(Point(i,j), (lines_[i][j] == '#'), self.size)
            lights[Point(i,j)] = light

        return lights
    
    def step(self, step_: int, stuck_: bool = False) -> int:
        count = 0
        states = dict()
        results = self.lights.copy()
        
        for i in range(step_):
            for light in results.values():
                states[light.point] = light.update(results)
     
            for point in states.keys():
                if (stuck_ and ((point == Point(0,0) or (point == Point(0,self.size - 1)) or (point == Point(self.size - 1,0)) or (point == Point(self.size - 1,self.size - 1))))):
                    continue
                results[point].state = states[point]
                
        for light in results.values():
            if light.state:
                count += 1
                
        return count
            
    def run(self):
        step = 100
        
        lines = readLines(self.filename)
        self.size = len(lines)
        
        # Part 1
        self.lights = self.loadLights(lines)
        self.result1 = self.step(step)
                
        # Part 2
        self.lights = self.loadLights(lines)
        self.lights[Point(0,0)].state = True
        self.lights[Point(0,self.size-1)].state = True
        self.lights[Point(self.size-1,0)].state = True
        self.lights[Point(self.size-1,self.size-1)].state = True
        self.result2 = self.step(step, True)
    
        return            
