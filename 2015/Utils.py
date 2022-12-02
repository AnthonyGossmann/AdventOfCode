############################################################
# Import
############################################################
from typing import List
from typing import Callable
import re
import sys

############################################################
# Utilities
############################################################
def readFile(filename: str) -> str:
    try:
        f = open(filename, 'r', encoding='utf-8')
        return f.read()
    except IOError:
        print(f"Error when opening \"{filename}\" file.")
        sys.exit(1)
        
def readLines(filename: str) -> List:
    try:
        f = open(filename, 'r', encoding='utf-8')
        return [line.strip() for line in f]
    except IOError:
        print(f"Error when opening \"{filename}\" file.")
        sys.exit(1)

def readSplit(filename: str, rgx: str) -> List:
    text = readFile(filename)
    return list(filter(None, re.split(rgx, text)))

def apply(clb: Callable, data: List) -> List:
    return [clb(i) for i in data]
