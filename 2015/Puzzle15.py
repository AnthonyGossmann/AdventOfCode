############################################################
# Import
############################################################
from Utils import *
from itertools import product
import typing
from typing import List
from typing import NewType
from dataclasses import dataclass
import re

############################################################
# Class Component
############################################################
Component = typing.NewType("Component ", None)
@dataclass()
class Component:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int
    
    def __init__(self, name_: str, capacity_: int, durability_: int, flavor_: int, texture_: int, calories_: int):
        self.name = name_
        self.capacity = capacity_
        self.durability = durability_
        self.flavor = flavor_
        self.texture = texture_
        self.calories = calories_
        
    def getProperties(self) -> List[int]:
        return [self.capacity, self.durability, self.flavor, self.texture, self.calories]

############################################################
# Class Puzzle15
############################################################
class Puzzle15:
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

        ingredients = dict()
        for line in lines:
            found = re.fullmatch(
                "(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)", line)
            ingredients[found.group(1)] = Component(found.group(1), int(found.group(2)), int(found.group(3)), int(found.group(4)), int(found.group(5)), int(found.group(6)))

        coefficients = [range(101) for i in ingredients]
        for coeff in product(*coefficients):
            if (sum(coeff) != 100):
                continue

            properties = [0, 0, 0, 0, 0]
            for i in range(len(coeff)):
                for j in range(len(properties)):
                    key = list(ingredients.keys())[i]
                    properties[j] += list(ingredients[key].getProperties())[j] * coeff[i]
                    
            properties = [max(0,x) for x in properties]
            score = properties[0] * properties[1] * properties[2] * properties[3]
            
            self.result1 = max(self.result1, score)
            
            if (properties[4] == 500):
                self.result2 = max(self.result2, score)

        return
