# -*- coding: utf-8 -*-
from entities.base.EntityProjectile import EntityProjectile

class EntityArrow(EntityProjectile):
    
    def __init__(self, game, owner, x, y, direct):
        self.speed = 5
        EntityProjectile.__init__(self, game, owner, x, y, self.speed, 80, direct)
        