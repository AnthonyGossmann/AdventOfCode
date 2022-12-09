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
Weapons = { (8,4), (10,5), (25,6), (40,7), (74,8) }
Armors = { (13,1), (31,2), (53,3), (75,4), (102,5) }
AttackRings = { (25,1), (50,2), (100,3) }
DefenceRings = { (20,1), (40,2), (80,3) }

############################################################
# Class Player
############################################################
Player = typing.NewType("Player", None)
@dataclass()
class Player:
    health: int
    damage: int
    armor: int
    currentHealth: int
    
    def __init__(self, health_: int, damage_: int, armor_: int):
        self.health = health_
        self.damage = damage_
        self.armor = armor_
        self.currentHealth = self.health
        
    def cure(self):
        self.currentHealth = self.health
        
    def attack(self, opponent_: Player) -> bool:
        return opponent_.defend(self.damage)
    
    def defend(self, damage_: int) -> bool:
        self.currentHealth -= max(damage_ - self.armor, 1)
        return (self.currentHealth <= 0)

############################################################
# Class Puzzle21
############################################################
class Puzzle21:
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
    
    def fight(self, player_: Player, boss_: Player) -> bool:
        while True:
            if player_.attack(boss_):
                return True
            if boss_.attack(player_):
                return False

    def gearUp(self, damage_: int, armor_: int) -> List[int]:
        attack_kits = []
        defence_kits = []
        
        # Attack
        for weapon in Weapons:
            if (weapon[1] < damage_):
                for rings in chain(combinations(AttackRings, 1), combinations(AttackRings, 2)):
                    rAttack = sum(x[1] for x in rings)
                    if (rAttack == (damage_ - weapon[1])):
                        attack_kits.append({ "weapon": weapon, "rings": rings })
                        
            elif (weapon[1] == damage_):
                attack_kits.append({ "weapon": weapon, "rings": [] })
        
        # Defence
        if (armor_ == 0):
            defence_kits.append({ "armor": (0,0), "rings": []})
        else:
            for rings in chain(combinations(DefenceRings, 1), combinations(DefenceRings, 2)):
                rDefence = sum(x[1] for x in rings)
                if (rDefence == armor_):
                    defence_kits.append({ "armor": (0,0), "rings": rings })
                    
            for armor in Armors:
                if (armor[1] < armor_):
                    for rings in chain(combinations(DefenceRings, 1), combinations(DefenceRings, 2)):
                        rDefence = sum(x[1] for x in rings)
                        if (rDefence == (armor_ - armor[1])):
                            defence_kits.append({ "armor": armor, "rings": rings })
                elif (armor[1] == armor_):
                    defence_kits.append({ "armor": armor, "rings": [] })
        
        # Kits
        costs = []
        for aKit, dKit in product(attack_kits, defence_kits):
            if ((len(aKit["rings"]) + len(dKit["rings"])) > 2):
                continue
            cost = aKit["weapon"][0] + dKit["armor"][0]
            cost += sum(x[0] for x in aKit["rings"])
            cost += sum(x[0] for x in dKit["rings"])
            costs.append(cost)
            
        return costs

    def run(self):
        text = re.sub("[ a-zA-z:]", "", readFile(self.filename))
        tokens = text.split('\n')
        boss = Player(int(tokens[0]), int(tokens[1]), int(tokens[2]))

        # Part 1
        costs = []
        for damage,armor in product(range(4, 14), range(11)):
            boss.cure()
            player = Player(100, damage, armor)
     
            if (self.fight(player, boss)):
                costs += self.gearUp(damage, armor) 
       
        self.result1 = min(costs)
        
        # Part 2
        costs = []
        for damage,armor in product(range(4, 14), range(11)):
            boss.cure()
            player = Player(100, damage, armor)
            
            if not self.fight(player, boss):
                costs += self.gearUp(damage, armor)
                
        self.result2 = max(costs)
       
        return            
