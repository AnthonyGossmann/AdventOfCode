############################################################
# Import
############################################################
from Utils import *
from itertools import product
import typing
from typing import Dict
from typing import List
from typing import NewType
from dataclasses import dataclass
from enum import Enum
import re

############################################################
# Class Point
############################################################
Point = typing.NewType("Point", None)
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
# Class Puzzle9
############################################################
class Puzzle9:
    filename: str
    result1: int
    result2: int
    
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def getNeighbours(self, point_: Point) -> List[Point]:
        x = [i for i in range(point_.x-1,point_.x+2)]
        y = [i for i in range(point_.y-1,point_.y+2)]
        
        ngh = []
        for i,j in product(x,y):
            ngh.append(Point(i,j))
        
        return ngh
    
    def moveHead(self, head_: Point, cmd_: str) -> Point:
        if (cmd_ == 'D'):
            head_.y -= 1
        elif (cmd_ == 'U'):
            head_.y += 1
        elif (cmd_ == 'L'):
            head_.x -= 1
        else:
            head_.x += 1
            
        return head_
    
    def move(self, current_: Point, next_: Point) -> Point:        
        if (tail_ not in self.getNeighbours(head_)):
            dx = (current_.x - next_.x)
            dy = (current_.y - next_.y)
            
            if (dx < -1):
                dx = -1
            elif (dx > 1):
                dx = 1
            
            if (dy < -1):
                dy = -1
            elif (dy > 1):
                dy = 1
                
            next_.x += dx
            next_.y += dy
                        
        return next_
    
    def move10(self, ropes_: List[Point], cmd_: str) -> List[Point]:
        ropes_[0] = self.moveHead(ropes_[0], cmd_)
        
        for i in range(1, 10):
            ropes_[i] = self.move(ropes_[i-1], ropes_[i])          
            
        return ropes_
            

    def run(self):
        lines = readLines(self.filename)

        # Part 1
        ropes = [Point(0,0), Point(0,0)]
        points = [Point(0,0)]
        
        for line in lines:
            tokens = line.split(" ")
            for i in range(int(tokens[1])):
                ropes[0] = self.moveHead(ropes[0], tokens[0])
                ropes[1] = self.move(ropes[0], ropes[1])
                if ropes[1] not in points:
                    points.append(Point(ropes[1].x,ropes[1].y))
            
        self.result1 = len(points)
        
        # Part 2
        ropes = [Point(0,0) for i in range(10)]
        points = [Point(0,0)]
        
        for line in lines:
            tokens = line.split(" ")
            for i in range(int(tokens[1])):
                ropes = self.move10(ropes, tokens[0])
                if ropes[-1] not in points:
                    points.append(Point(ropes[-1].x,ropes[-1].y))

        self.result2 = len(points)
        
        return            
