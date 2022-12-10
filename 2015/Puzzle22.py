############################################################
# Import
############################################################
from Utils import *
import typing
from typing import NewType
from dataclasses import dataclass

# import copy
# import typing
# from typing import Dict
# from typing import List
# import re

############################################################
# Class State
############################################################
State = typing.NewType("State", None)
@dataclass()
class State:
    boss_hp: int
    boss_damage: int
    player_hp: int
    player_armor: int
    player_mana: int
    poison_timer: int
    shield_timer: int
    recharge_timer: int
    
############################################################
# Spells
############################################################
MAGIC_MISSILE = 53
def magicMissile(state_: State) -> State:
    state_.player_mana -= MAGIC_MISSILE
    state_.boss_hp -= 4
    return state_

DRAIN = 73
def drain(state_: State) -> State:
    state_.player_mana -= DRAIN
    state_.player_hp += 2
    state_.boss_hp -= 2
    return state_

SHIELD = 113
def shield(state_: State) -> State:
    state_.player_mana -= SHIELD
    state_.player_armor = 7
    state_.shield_timer = 6
    return state_

POISON = 173
def poison(state_: State) -> State:
    state_.player_mana -= POISON
    state_.poison_timer = 6
    return state_

RECHARGE = 229
def recharge(state_: State) -> State:
    state_.player_mana -= RECHARGE
    state_.recharge_timer = 5
    return state_

############################################################
# Methods
############################################################
def applyEffects(state_: State) -> State:
    if (state_.shield_timer > 0):
        state_.shield_timer -= 1
        if (state_.shield_timer == 0):
            state_.player_armor = 0
    if (state_.poison_timer > 0):
        state_.boss_hp -= 3
        state_.poison_timer -= 1
    if (state_.recharge_timer > 0):
        state_.player_mana += 101
        state_.recharge_timer -= 1
        
    return state_

def bossAttack(state_: State) -> State:
    state_.player_hp -= max(state_.boss_damage - state_.player_armor, 1)
    return state_

def fightRound(state_: State) -> int:
    if (state_.boss_hp <= 0):
        return 0
    elif (state_.player_hp <= 0):
        return -1
    
    # Apply Effects
    state_ = applyEffects(state_)
    if (state_.boss_hp <= 0):
        return 0
    
    # Player
    options = []
    if (state_.player_mana > MAGIC_MISSILE):
        state = magicMissile(state_)
        options.append((fightRound(state), MAGIC_MISSILE)
    if (state_.player_mana > DRAIN):
        state = magicMissile(state_)
        options.append((fightRound(state), MAGIC_MISSILE)
    if (state_.player_mana > SHIELD):
        options.append((fightRound(shield(state_)), SHIELD))
    if (state_.player_mana > MAGIC_MISSILE):
        options.append((fightRound(magicMissile(state_)), MAGIC_MISSILE))
    if (state_.player_mana > MAGIC_MISSILE):
        options.append((fightRound(magicMissile(state_)), MAGIC_MISSILE))

# ############################################################
# # Definitions
# ############################################################
# Spells = {
#     "Magic Missile": {"cost": 53,  "damage": 4, "health": 0, "armor": 0, "mana": 0,   "time": 0},
#     "Drain"        : {"cost": 73,  "damage": 2, "health": 2, "armor": 0, "mana": 0,   "time": 0},
#     "Shield"       : {"cost": 113, "damage": 0, "health": 0, "armor": 7, "mana": 0,   "time": 6},
#     "Poison"       : {"cost": 173, "damage": 3, "health": 0, "armor": 0, "mana": 0,   "time": 6},
#     "Recharge"     : {"cost": 229, "damage": 0, "health": 0, "armor": 0, "mana": 101, "time": 5}
# }

# ############################################################
# # Class Player
# ############################################################
# Player = typing.NewType("Player", None)
# @dataclass()
# class Player:
#     wizard: bool
#     health: int
#     damage: int
#     armor: int
#     mana: int
#     currentHealth: int
#     currentMana: int
#     cost: int
#     timers: Dict[str,int]
    
#     def __init__(self, wizard_: bool, health_: int, damage_: int, armor_: int, mana_: int):
#         self.wizard = wizard_
#         self.health = health_
#         self.damage = damage_
#         self.armor = armor_
#         self.mana = mana_
#         self.cost = 0
#         self.timers = { "Shield": 0, "Poison": 0, "Recharge": 0}
        
    # def alive(self) -> bool:
    #     return (self.currentHealth > 0)
            
    # def canCast(self, spell_: str):   
    #     result = (self.currentMana >= Spells[spell_]["cost"])
    #     if (spell_ in self.timers.keys()):
    #         result &= (self.timers[spell_] == 0)
    #     return result
        
    # def effect(self, opponent_: Player) -> bool:
    #     # Mana
    #     if (self.timers["Recharge"] > 0):
    #         self.currentMana += Spells["Recharge"]["mana"]
    #         self.timers["Recharge"] -= 1
            
    #     # Armor
    #     if (self.timers["Shield"] > 0):
    #         self.armor = Spells["Shield"]["armor"]
    #         self.timers["Shield"] -= 1
    #         if (self.timers["Shield"] == 0):
    #             self.armor = 0
    #     else:
    #         self.armor = 0
            
    #     # Damage
    #     if (self.timers["Poison"] > 0):
    #         opponent_.defend(Spells["Poison"]["damage"])
    #         self.timers["Poison"] -= 1
        
    # def attack(self, opponent_: Player, spell_: str = ""):
    #     if self.wizard:
    #         self.cost += Spells[spell_]["cost"]
    #         self.currentMana -= Spells[spell_]["cost"]
    #         self.currentHealth += Spells[spell_]["health"]
            
    #         if (Spells[spell_]["time"] == 0):
    #             opponent_.defend(Spells[spell_]["damage"])
    #         else:
    #             self.timers[spell_] = Spells[spell_]["time"]     
    #     else:
    #         opponent_.defend(self.damage)
            
    # def defend(self, damage_: int):
    #     if self.wizard:
    #         self.currentHealth -= max(damage_ - self.armor, 1)
    #     else:
    #         self.currentHealth -= damage_
    
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
    
    # def status(self, player_: Player, boss_: Player):
    #     print("Player has " + str(player_.currentHealth) + " hit points, " + str(player_.armor) + " armor, " + str(player_.currentMana) + " mana")
    #     print("Boss has " + str(boss_.currentHealth) + " hit points")
        
    # def test(self):
    #     #boss = Player(False, 13, 8, 0, 0)
    #     boss = Player(False, 14, 8, 0, 0)
    #     player = Player(True, 10, 0, 0, 250)
        
    #     #spells = ["Poison", "Magic Missile"]
    #     spells = ["Recharge", "Shield", "Drain", "Poison", "Magic Missile"]
        
    #     for spell in spells:
    #         self.status(player, boss)
            
    #         print("-- Player turn --")
    #         self.status(player, boss)
    #         player.effect(boss)
            
            
    #         if not boss.alive():
    #             print("Player wins")
    #             break
            
    #         if not player.canCast(spell):
    #             print("Boss wins")
    #             break
            
    #         print("Player casts " + spell)
    #         player.attack(boss, spell)
            
    #         if not boss.alive():
    #             print("Player wins")
    #             break

    #         print("-- Boss turn --")
    #         self.status(player, boss)
    #         player.effect(boss)
            
    #         if not boss.alive():
    #             print("Player wins")
    #             break
            
    #         print("Boss attacks for " + str(boss.damage) + " damage")
    #         boss.attack(player)

    #         if not player.alive():
    #             print("Boss wins")
    #             break

    # def turn(self, player_: Player, boss_: Player):
    #     mana = []
    #     scenarii = []
        
    #     # Effect
    #     player_.effect(boss_)
    #     if not boss_.alive():
    #         mana.append(player_.cost)
    #         return [scenarii, mana]
        
    #     # Select spell
    #     spell = []
    #     for s in Spells.keys():
    #         if player_.canCast(s):
    #             spell.append(s)
        
    #     if (len(spell) == 0):
    #         return [scenarii, mana]
        
    #     # Attack
    #     for s in spell:
    #         player = copy.copy(player_) 
    #         boss = copy.copy(boss_)
            
    #         player.attack(boss, s)
            
    #         if not boss.alive():
    #             mana.append(player.cost)
    #             continue
            
    #         player.effect(boss)
            
    #         if not boss.alive():
    #             mana.append(player.cost)
    #             continue
            
    #         boss.attack(player)
            
    #         if not player.alive():
    #             return [scenarii, mana]
            
    #         scenarii.append((player,boss))
            
    #     return [scenarii, mana]
            

    def run(self):
        #self.test()
        
        # text = re.sub("[ a-zA-z:]", "", readFile(self.filename))
        # tokens = text.split('\n')
        
        # boss = Player(False, int(tokens[0]), int(tokens[1]), 0, 0)
        # player = Player(True, 50, 0, 0, 500)
        
        # scenarii = [(player,boss)]
        # wMana = []

        # while (len(scenarii) != 0):
        #     ns = []
        #     for scenario in scenarii:
        #         [sc, mana] = self.turn(scenario[0], scenario[1])
        #         ns += sc
        #         wMana += mana
                
        #     scenarii.clear()
        #     scenarii = copy.copy(ns)
        
        # self.result1 = min(wMana)
            
            
        

        return            
