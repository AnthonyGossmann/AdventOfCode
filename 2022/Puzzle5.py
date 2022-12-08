############################################################
# Import
############################################################
from Utils import *
import typing
from typing import Dict
from typing import List
from typing import NewType
from dataclasses import dataclass
import re

############################################################
# Class Command
############################################################
Command = typing.NewType("Command", None)
@dataclass()
class Command:
    size: int
    start: int
    end: int

############################################################
# Class Stack
############################################################
Stack = typing.NewType("Stack", None)
@dataclass()
class Stack:
    name: int
    crates: List[str]

############################################################
# Class Puzzle5
############################################################
class Puzzle5:
    def __init__(self, filename_: str):
        self.filename: str = filename_
        self.result1: str = ""
        self.result2: str = ""
    
    def getResult1(self) -> str:
        return self.result1

    def getResult2(self) -> str:
        return self.result2
    
    def loadStacks(self) -> [Dict[int,Stack], List[Command]]:
        text = readFile(self.filename)
        lines = text.split("\n")
        
        stacks = dict()
        commands = list()
        for line in lines:
            if ('[' in line):
                # Load Stacks
                line = re.sub("[\[\]]", "", line)
                tokens = re.split("[\s]{4}", line)
                
                crates = []
                for token in tokens:
                    crates += re.split(" ", token)
                
                for i in range(len(crates)):
                    if (i+1) not in stacks.keys():
                        stacks[i+1] = Stack(i+1, [])
                    if (crates[i] != ''):
                        stacks[i+1].crates.insert(0, crates[i])
                        
            elif ("move" in line):
                 found =  re.fullmatch("move (.+) from (.+) to (.+)", line)
                 commands.append(Command(int(found.group(1)), int(found.group(2)), int(found.group(3))))

        return [stacks, commands]
    
    def move(self, stacks_: Dict[int,Stack], command_: Command, crateMover9001_: bool = False):
        if crateMover9001_:
                items = stacks_[command_.start].crates[-command_.size:]
                stacks_[command_.start].crates = stacks_[command_.start].crates[:-command_.size]
                stacks_[command_.end].crates += items
        else:
            for i in range(command_.size):
                item = stacks_[command_.start].crates[-1]
                stacks_[command_.start].crates = stacks_[command_.start].crates[:-1]
                stacks_[command_.end].crates.append(item)
            
        return stacks_
    
    def getTop(self, stacks_: Dict[int, Stack]) -> str:
        result = ""
        for stack in stacks_.values():
            if (len(stack.crates) != 0):
                result += stack.crates[-1]
        return result

    def run(self):
        text = readFile(self.filename)
        lines = text.split("\n")
        
        # Part 1
        [stacks, commands] = self.loadStacks()
        for cmd in commands:
            stacks = self.move(stacks, cmd)
        self.result1 = self.getTop(stacks)
        
        # Part 2
        [stacks, commands] = self.loadStacks()
        for cmd in commands:
            stacks = self.move(stacks, cmd, True)
        self.result2 = self.getTop(stacks)
        
        return            
