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
# Definitions
############################################################
Spells = {
    "Magic_Missile": {"cost": 53, "damage": 4},
    "Drain"        : {"cost": 73, "damage": 2, "health": 2},
    "Shield"       : {"cost": 113, "armor": 7, "time": 6},
    "Poison"       : {"cost": 173, "damage": 3, "time": 6},
    "Recharge"     : {"cost": 229, "mana": 101, "time": 5}
}

############################################################
# Class Player
############################################################
Player = typing.NewType("Player", None)
@dataclass()
class Player:
    wizard: bool
    health: int
    damage: int
    armor: int
    mana: int
    currentHealth: int
    currentMana: int
    cost: int
    spells: Dict[str,int]
    
    def __init__(self, wizard_: bool, health_: int, damage_: int, armor_: int, mana_: int):
        self.wizard = wizard_
        self.health = health_
        self.damage = damage_
        self.armor = armor_
        self.mana = mana_
        self.currentHealth = health_
        self.currentMana = mana_
        self.cost = 0
        self.spells = {}
        
    def cure(self):
        self.currentHealth = self.health
        self.currentMana = self.mana
        
    def effect(self) -> List[int]:
        damage = 0
        armor = 0
        mana = 0
        
        # Effect
        if ("Poison" in self.spells.keys()):
            damage += Spells["Poison"]["damage"]
        if ("Shield" in self.spells.keys()):
            armor += Spells["Shield"]["armor"]
        if ("Recharge" in self.spells.keys()):
            mana += Spells["Recharge"]["mana"]
        
        # Timers
        for spell in self.spells.keys():
            self.spells[spell] -= 1
            if (self.spells[spell] == 0):
                self.spells.pop[spell]
            
        return [damage, armor, mana]
            
        
    def attack(self, opponent_: Player, spell_: str = "") -> bool:
        if self.wizard:
            # Effects
            [damage, armor, mana] = self.effect()
            if (spell_ in self.spells.keys()):
                return False
            
            # Update status
            self.armor = armor
            self.currentMana += mana
            if opponent_.defend(self, damage):
                return True
        
            # Cast
            if (self.mana < Spells[spell_]["cost"]):
                return False
            
            # Cost
            self.cost += Spells[spell_]["cost"]
            self.currentMana -= Spells[spell_]["cost"]
            
            # Action
            if (spell_ == "Magic_Missile"):
                if opponent_.defend(self, Spells[spell_]["damage"]):
                    return True
            elif (spell_ == "Drain"):
                if opponent_.defend(self, Spells[spell_]["damage"]):
                    return True
                self.currentHealth += Spells[spell_]["health"]
            else:
                self.spells[spell_] = Spells[spell_]["time"]
        else:
            return opponent_.defend(self, self.damage)
        
    def defend(self, opponent_: Player, damage_: int) -> bool:
        if (self.wizard):
            # Effects
            [damage, armor, mana] = self.effect()
            
            # Update status
            self.armor = armor
            self.currentMana += mana
            if opponent_.defend(self, damage):
                return False

            self.currentHealth -= max(damage_ - self.armor, 1)      
        else:
            self.currentHealth -= damage_
            
        return (self.currentHealth <= 0)
    
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
    
    def test(self):
        boss = Player(False, 13, 8, 0, 0)
        player = Player(True, 10, 0, 0, 250)
        
        print("-- Player turn --")
        win = player.attack(boss, "Poison")
        print("Player has " + str(player.currentHealth) + " hit points, " + str(player.armor) + " armor, " + str(player.currentMana) + " mana")
        print("Boss has " + str(boss.currentHealth) + " hit points")
        print("Player win: " + str(win))
        
        print("-- Boss turn --")
        win = boss.attack(player)
        print("Player has " + str(player.currentHealth) + " hit points, " + str(player.armor) + " armor, " + str(player.currentMana) + " mana")
        print("Boss has " + str(boss.currentHealth) + " hit points")
        print("Player win: " + str(win))
        
        print("-- Player turn --")
        win = player.attack(boss, "Magic_Missile")
        print("Player has " + str(player.currentHealth) + " hit points, " + str(player.armor) + " armor, " + str(player.currentMana) + " mana")
        print("Boss has " + str(boss.currentHealth) + " hit points")
        print("Player win: " + str(win))
        
        print("-- Boss turn --")
        win = boss.attack(player)
        print("Player has " + str(player.currentHealth) + " hit points, " + str(player.armor) + " armor, " + str(player.currentMana) + " mana")
        print("Boss has " + str(boss.currentHealth) + " hit points")
        print("Player win: " + str(win))

    def run(self):
        self.test()
        return            
