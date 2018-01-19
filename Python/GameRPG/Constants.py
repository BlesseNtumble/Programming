SIZE = (WIDTH, HEIGHT) = (1250, 916)

HUD_PANEL_SIZE = 80

LEVELS = 20
EXP = []
HP = []
MP = []
for i in range(LEVELS):
    EXP.append(568 + 500*i)
    HP.append(100 + 40*i)
    MP.append(300 + 40*i)

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
SPEED = 3
SPELL_COST = 10
HP_REG = 1
MP_REG = 1


# Monster Type
PASSIVE = 0
AGRESSIVE = 1
AGRESSIVE_AFTER_ATTACK = 2

# Attack Type
MELEE = 0
RANGE = 1