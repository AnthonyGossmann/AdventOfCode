############################################################
# Configuration
############################################################
# Puzzle Number
PUZZLE = 2
# Use example input
USE_EXAMPLE = 0

############################################################
# Import
############################################################
from Puzzle1 import *
from Puzzle2 import *
from Puzzle3 import *
from Puzzle4 import *
from Puzzle5 import *
from Puzzle6 import *
from Puzzle7 import *
from Puzzle8 import *
from Puzzle9 import *
from Puzzle10 import *
from Puzzle11 import *
from Puzzle12 import *
from Puzzle13 import *
from Puzzle14 import *
from Puzzle15 import *
from Puzzle16 import *
from Puzzle17 import *
from Puzzle18 import *
from Puzzle19 import *
from Puzzle20 import *
from Puzzle21 import *
from Puzzle22 import *
from Puzzle23 import *
from Puzzle24 import *
from Puzzle25 import *

############################################################
# Main
############################################################
testStr = ('0' + str(PUZZLE)) if (len(str(PUZZLE)) != 2) else str(PUZZLE)
testInput = ("data/" + testStr + ".ex") if (USE_EXAMPLE == 1) else ("data/" + testStr + ".txt")

if (PUZZLE == 1):
    p = Puzzle1(testInput)
elif (PUZZLE == 2):
    p = Puzzle2(testInput)
elif (PUZZLE == 3):
    p = Puzzle3(testInput)
elif (PUZZLE == 4):
    p = Puzzle4(testInput)   
elif (PUZZLE == 5):
    p = Puzzle5(testInput)
elif (PUZZLE == 6):
    p = Puzzle6(testInput)
elif (PUZZLE == 7):
    p = Puzzle7(testInput)
elif (PUZZLE == 8):
    p = Puzzle8(testInput)
elif (PUZZLE == 9):
    p = Puzzle9(testInput)
elif (PUZZLE == 10):
    p = Puzzle10(testInput)
elif (PUZZLE == 11):
    p = Puzzle11(testInput)
elif (PUZZLE == 12):
    p = Puzzle12(testInput)
elif (PUZZLE == 13):
    p = Puzzle13(testInput)
elif (PUZZLE == 14):
    p = Puzzle14(testInput)
elif (PUZZLE == 15):
    p = Puzzle15(testInput)
elif (PUZZLE == 16):
    p = Puzzle16(testInput)
elif (PUZZLE == 17):
    p = Puzzle17(testInput)
elif (PUZZLE == 18):
    p = Puzzle18(testInput)
elif (PUZZLE == 19):
    p = Puzzle19(testInput)
elif (PUZZLE == 20):
    p = Puzzle20(testInput)
elif (PUZZLE == 21):
    p = Puzzle21(testInput)
elif (PUZZLE == 22):
    p = Puzzle22(testInput)
elif (PUZZLE == 23):
    p = Puzzle23(testInput)
elif (PUZZLE == 24):
    p = Puzzle24(testInput)
else:
    p = Puzzle25(testInput)
 
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))
