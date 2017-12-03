import random


SIZE = (WIDTH, HEIGHT) = (1250, 916)

LEVELS = 20
EXP = []
for i in range(LEVELS):
    EXP.append(100 + 500*i + random.randint(0, 100))
    
print(EXP)
# Direction
DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3

# Status
ALIVE = 1
DEAD = 3
SHOOT = 4

# Chars
SPEED = 1
SPELL_COST = 10
HP_REG = 1
MP_REG = 1
