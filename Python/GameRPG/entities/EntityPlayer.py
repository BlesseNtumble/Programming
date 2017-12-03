# -*- coding: utf-8 -*-
from Constants import *
from entities.base.EntityLiving import *
from skills.Skills import Skills, Arrow


position = [150, 50]

class EntityPlayer(EntityLiving):
    
    def __init__(self, game):
        self.name = 'Little Boy'
        self.game = game
        self.chars = [100, 100, SPEED] #HP, MP, SPEED
        self.base = [self.chars[0], self.chars[1], position[0], position[1], HP_REG, MP_REG, SPEED]       
        EntityLiving.__init__(self, self.game, self.name, self.chars, self.base, DOWN, ALIVE, position, 'PLAYER')    
    
        self.skill_list.append(Arrow(self))
    
    def useSkill(self, skillid):        
        self.skill_list[skillid].useSkill()
        
    def tick(self):
        EntityLiving.tick(self)
        [i.tick() for i in self.skill_list]

    def render_ui(self, screen, camera): 
        EntityLiving.render_ui(self, screen, camera, True)