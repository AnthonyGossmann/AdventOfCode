############################################################
# Import
############################################################
from Utils import *
from itertools import chain, combinations, product
import typing
from typing import Dict
from typing import List
from typing import NewType
from dataclasses import dataclass
import re

############################################################
# Class Fighter
############################################################
Fighter = typing.NewType("Fighter", None)
@dataclass()
class Fighter:
    name: str
    health: int
    damage: int
    armor: int
    startHealth: int
    
    def __init__(self, name_: str, health_: int, damage_: int, armor_: int):
        self.name = name_
        self.health = health_
        self.damage = damage_
        self.armor = armor_
        self.startHealth = self.health
        
    def cure(self):
        self.health = self.startHealth
        
    def attack(self, opponent_: Wizard) -> bool:
        return opponent_.defend(self.damage)
    
    def defend(self, damage_: int) -> bool:
        self.health -= max(damage_ - self.armor, 1)
        return (self.health <= 0)
    
############################################################
# Class Wizard
############################################################
Wizard = typing.NewType("Wizard", None)
@dataclass()
class Wizard:
    name: str
    health: int
    damage: int
    armor: int
    startHealth: int
    
    def __init__(self, name_: str, health_: int, damage_: int, armor_: int):
        self.name = name_
        self.health = health_
        self.damage = damage_
        self.armor = armor_
        self.startHealth = self.health
        
    def cure(self):
        self.health = self.startHealth
        
    def attack(self, opponent_: Fighter) -> bool:
        return opponent_.defend(self.damage)
    
    def defend(self, damage_: int) -> bool:
        self.health -= max(damage_ - self.armor, 1)
        return (self.health <= 0)

############################################################
# Class Puzzle22
############################################################
class Puzzle22:
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

    def run(self):
    
        return            
