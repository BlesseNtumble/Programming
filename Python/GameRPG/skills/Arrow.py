from entities import EntityArrow
from skills import *


class Arrow(Skills):
    
    def __init__(self, game, caster):
        self.game = game
        self.cost = 5
        Skills.__init__(self, game, self.cost, caster)
       
    def action(self):
        self.game.projectiles.append(EntityArrow(self, self.game.player.posX, self.game.player.posY, self.game.player.direction))
