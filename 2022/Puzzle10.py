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
# Class Command
############################################################
Command = typing.NewType("Command", None)
@dataclass()
class Command:
    cycle: int
    value: int
    
    def __init__(self, cycle_: int, value_: int):
        self.cycle = cycle_
        self.value = value_

############################################################
# Class Puzzle10
############################################################
class Puzzle10:
    filename: str
    result1: int
    result2: int

    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = "\n"

        self.x = 1
        self.cycle = 0
        self.commands = []

    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> str:
        return self.result2

    def command(self, commands_: List[Command], cycle_: int, x_: int) -> int:
        for cmd in commands_:
            if (cmd.cycle == cycle_):
                x_ += cmd.value
        return x_

    def run(self):
        lines = readLines(self.filename)
        
        # Load Commands
        cycle = 0
        commands = []
        for line in lines:
            if ("noop" in line):
                cycle += 1
            elif ("addx" in line):
                cycle += 2
                value = int(re.split(" ", line)[-1])
                commands.append(Command(cycle + 1, value)) 
                
        # Part 1
        cycle = 0
        x = 1
        for i in range(220):
            cycle += 1
            x = self.command(commands, cycle, x)
            
            if ((cycle % 40) == 20):
                self.result1 += cycle * x
                
        # Part 2
        cycle = 0
        x = 1
        width = 40

        for i in range(240):
            cycle += 1
            x = self.command(commands, cycle, x)
            
            col = (cycle - 1) % width   
            if (x in [col-1, col, col+1]):
                self.result2 += '#'
            else:
                self.result2 += '.'
                
            if (col == (width-1)):
                self.result2 += '\n'

        return
