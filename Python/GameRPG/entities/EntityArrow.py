# -*- coding: utf-8 -*-
from entities.base.EntityProjectile import EntityProjectile

class EntityArrow(EntityProjectile):
    
    def __init__(self, game, owner, x, y, direct):
        self.game = game
        self.speed = 8
        self.image = self.game.assets['ARROW'][direct]
        EntityProjectile.__init__(self, game, owner, self.image, x, y, self.speed, 80, 350, direct)
        