############################################################
# Import
############################################################
from Utils import *
import typing
from typing import List
from typing import NewType
from dataclasses import dataclass
import numpy as np

############################################################
# Class Reindeer
############################################################
Reindeer = typing.NewType("Reindeer ", None)
@dataclass()
class Reindeer:
    name: str
    speed: int
    time: int
    rest: int
    
    def __init__(self, name_: str, speed_: int, time_: int, rest_: int):
        self.name = name_
        self.speed = speed_
        self.time = time_
        self.rest = rest_
    
    def distance(self, time_: int) -> int:
        distance = 0
        
        tFrame = self.time + self.rest
        nFrame = time_ // tFrame
        distance = nFrame * self.speed * self.time
        
        tRemain = time_ - nFrame * tFrame
        distance += self.speed * min(tRemain, self.time)
        
        return distance

############################################################
# Class Puzzle14
############################################################
class Puzzle14:
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

        reindeers = dict()
        for line in lines:
            found = re.fullmatch("(.+) can fly (.+) km/s for (.+) seconds, but then must rest for (.+) seconds.", line)
            reindeers[found.group(1)] = Reindeer(found.group(1), int(found.group(2)), int(found.group(3)), int(found.group(4)))
            
        # Part 1
        for r in reindeers.values():
            self.result1 = max(self.result1, r.distance(2503))
            
        # Part 2
        points = dict.fromkeys(reindeers.keys(), 0)
        for t in range(1, 2503):
            distance = dict.fromkeys(reindeers.keys(), 0)
            for reindeer in reindeers.values():
                distance[reindeer.name] = reindeer.distance(t)
            for reindeer in distance.keys():
                if (distance[reindeer] == max(distance.values())):
                    points[reindeer] += 1
        self.result2 = max(points.values())
        
        return            
