# -*- coding: utf-8 -*-
from entities.base.EntityProjectile import EntityProjectile

class EntityArrow(EntityProjectile):
    
    def __init__(self, game, x, y, direct):
        self.image = ['resources/arrow.png', 1, 4, 48]
        self.speed = 5
        EntityProjectile.__init__(self, game, x, y, self.speed, 10, direct, self.image)
        