############################################################
# Import
############################################################
from Utils import *
from itertools import chain, combinations, product
import copy
import typing
from typing import Dict
from typing import List
from typing import NewType
from dataclasses import dataclass
import re

############################################################
# Class Game
############################################################
Game = typing.NewType("Game", None)
@dataclass
class Game:
    boss_hp: int
    boss_dmg: int
    player_hp: int
    player_arm: int
    player_mana: int
    player_cost: int
    timer_poison: int
    timer_shield: int
    timer_recharge: int
    player_turn: bool
    hard_rules: bool

############################################################
# Spells
############################################################
MAGIC_MISSILE = 53
def magicMissile(game_: Game) -> Game:
    game_.player_cost += MAGIC_MISSILE
    game_.player_mana -= MAGIC_MISSILE
    game_.boss_hp -= 4
    return game_

DRAIN = 73
def drain(game_: Game) -> Game:
    game_.player_cost += DRAIN
    game_.player_mana -= DRAIN
    game_.player_hp += 2
    game_.boss_hp -= 2
    return game_

SHIELD = 113
def shield(game_: Game) -> Game:
    game_.player_cost += SHIELD
    game_.player_mana -= SHIELD
    game_.player_arm = 7
    game_.timer_shield = 6
    return game_

POISON = 173
def poison(game_: Game) -> Game:
    game_.player_cost += POISON
    game_.player_mana -= POISON
    game_.timer_poison = 6
    return game_

RECHARGE = 229
def recharge(game_: Game) -> Game:
    game_.player_cost += RECHARGE
    game_.player_mana -= RECHARGE
    game_.timer_recharge = 5
    return game_

def isCastValid(game_: Game, cast_: int) -> bool:
    if (game_.player_mana < cast_):
        return False
    
    if ((cast_ == SHIELD) and (game_.timer_shield != 0)):
        return False
    
    if ((cast_ == POISON) and (game_.timer_poison != 0)):
        return False
    
    if ((cast_ == RECHARGE) and (game_.timer_recharge != 0)):
        return False
    
    return True


############################################################
# Attack/Effect
############################################################
def applyEffect(game_: Game) -> Game:
    # Shield
    if (game_.timer_shield > 0):
        game_.timer_shield -= 1
        if (game_.timer_shield == 0):
            game_.player_arm = 0
    # Poison
    if (game_.timer_poison > 0):
        game_.timer_poison -= 1
        game_.boss_hp -= 3
    # Mana
    if (game_.timer_recharge > 0):
        game_.timer_recharge -= 1
        game_.player_mana += 101
        
    return game_

def bossAttack(game_: Game) -> Game:
    game_.player_hp -= max(game_.boss_dmg - game_.player_arm, 1)
    return game_

############################################################
# Round
############################################################

    
############################################################
# Class Puzzle22
############################################################
class Puzzle22:
    filename: str
    result1: int
    result2: int
    
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 1E9
        self.result2 = 1E9
        self.cost = 1E9

    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def fightRound(self, game_: Game) -> int:
        if (game_.player_cost > self.cost):
            return -1
        
        # Check
        if (game_.boss_hp <= 0):
            self.cost = min(self.cost, game_.player_cost)
            return game_.player_cost
        if (game_.player_hp <= 0):
            return -1
        
        # Turn
        game_.player_turn = not game_.player_turn
        
        # Hard rules
        if (game_.player_turn and game_.hard_rules):
            game_.player_hp -= 1
            if (game_.player_hp <= 0):
                return -1
        
        # Effect
        game_ = applyEffect(game_)
        if (game_.boss_hp <= 0):
            self.cost = min(self.cost, game_.player_cost)
            return game_.player_cost
        
        # Attack
        if game_.player_turn:    
            # Players
            options = []
    
            if isCastValid(game_, MAGIC_MISSILE):
                options.append(self.fightRound(magicMissile(copy.copy(game_))))
            if isCastValid(game_, DRAIN):
                options.append(self.fightRound(drain(copy.copy(game_))))
            if isCastValid(game_, SHIELD):
                options.append(self.fightRound(shield(copy.copy(game_))))
            if isCastValid(game_, POISON):
                options.append(self.fightRound(poison(copy.copy(game_))))
            if isCastValid(game_, RECHARGE):
                options.append(self.fightRound(recharge(copy.copy(game_))))
    
            if (len(options) == 0):
                return -1
            elif all(x == -1 for x in options):
                return -1
            else:
                results = [x for x in options if x > 0]
                return min(results)
        else:
            return self.fightRound(bossAttack(game_))

    def run(self):
        # Part 1
        self.cost = 1E9
        game = Game(58, 9, 50, 0, 500, 0, 0, 0, 0, False, False)
        self.result1 = self.fightRound(game)
        
        # Part 2
        self.cost = 1E9
        game = Game(58, 9, 50, 0, 500, 0, 0, 0, 0, False, True)
        self.result2 = self.fightRound(game)
        
        return            
