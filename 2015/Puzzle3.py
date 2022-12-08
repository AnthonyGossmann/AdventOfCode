############################################################
# Import
############################################################
from Utils import *
import typing
from typing import List
from typing import NewType
from dataclasses import dataclass

############################################################
# Class House
############################################################
House = typing.NewType("House", None)
@dataclass()
class House:
    x: int
    y: int
    
############################################################
# Class Puzzle3
############################################################
class Puzzle3:
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
    
    def track(self, cmds_: str, start_: int = 0, step_: int = 1) -> List[House]:
        houses = [House(0,0)]
        x = 0
        y = 0
        
        for i in range(start_, len(cmds_), step_):
            if (cmds_[i] == "v"):
                y -= 1
            elif (cmds_[i] == "^"):
                y += 1
            elif (cmds_[i] == "<"):
                x -= 1
            else:
                x += 1

            house = House(x, y)
            if house not in houses:
                houses.append(house)
            
        return houses

    def run(self):
        text = readFile(self.filename)
        
        # Part 1
        houses = self.track(text)
        self.result1 = len(houses)
        
        # Part 2
        houses = self.track(text, 0, 2) + self.track(text, 1, 2)
        houses = [houses[i] for i in range(len(houses)) if i == houses.index(houses[i]) ]
        self.result2 = len(houses)
        
    
        return            
