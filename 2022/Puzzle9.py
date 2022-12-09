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
    
    def move(self, head_: Point, tail_: Point) -> Point:        
        if (tail_ not in self.getNeighbours(head_)):
            # Up
            if ((tail_.x == head_.x) and (head_.y > tail_.y)):
                tail_.y += 1
            # Down
            elif ((tail_.x == head_.x) and (head_.y < tail_.y)):
                tail_.y -= 1
            # Right
            elif ((tail_.y == head_.y) and (head_.x > tail_.x)):
                tail_.x += 1
            # Left
            elif ((tail_.y == head_.y) and (head_.x < tail_.x)):
                tail_.x -= 1
            # Up Right
            elif ((head_.x > tail_.x) and (head_.y > tail_.y)):
                tail_.x += 1
                tail_.y += 1
            # Down Right
            elif ((head_.x > tail_.x) and (head_.y < tail_.y)):
                tail_.x += 1
                tail_.y -= 1
            # Up Left
            elif ((head_.x < tail_.x) and (head_.y > tail_.y)):
                tail_.x -= 1
                tail_.y += 1
            # Down Left
            else:
                tail_.x -= 1
                tail_.y -= 1
                        
        return tail_
    
    def move10(self, head_: Point, ropes_: List[Point], cmd_: str):
        ropes = []
        head_ = self.moveHead(head_, cmd_)
        h = head_
        
        for i in range(9):
            t = ropes_[i]
            h = self.move(h, t)          
            ropes.append(h)
            
        return [head_, ropes]
            

    def run(self):
        lines = readLines(self.filename)

        # Part 1
        head = Point(0,0)
        tail = Point(0,0)
        points = [Point(0,0)]
        
        for line in lines:
            tokens = line.split(" ")
            for i in range(int(tokens[1])):
                head = self.moveHead(head, tokens[0])
                tail = self.move(head, tail)
                if tail not in points:
                    points.append(Point(tail.x,tail.y))
            
        self.result1 = len(points)
        
        # Part 2
        head = Point(0,0)
        ropes = [Point(0,0) for i in range(9)]
        points = [Point(0,0)]
        
        for line in lines:
            tokens = line.split(" ")
            for i in range(int(tokens[1])):
                [head, ropes] = self.move10(head, ropes, tokens[0])
                if ropes[-1] not in points:
                    points.append(Point(ropes[-1].x,ropes[-1].y))

        self.result2 = len(points)
        
        return            
