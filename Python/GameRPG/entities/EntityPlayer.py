# -*- coding: utf-8 -*-
from Constants import *
from entities.base.EntityLiving import *


position = [150, 50]
char_img = ['resources/actor.png', 4, 4, 48] # image, u, v, size

class EntityPlayer(EntityLiving):
    
    def __init__(self, game):
        self.name = 'Little Boy'
        self.game = game
        self.chars = [100, 100, SPEED] #HP, MP, SPEED
        self.base = [self.chars[0], self.chars[1], position[0], position[1]]
        EntityLiving.__init__(self, self.game, self.name, self.chars, self.base, DOWN, ALIVE, position, char_img)    
           
    
    def render_gui(self, screen):
        EntityLiving.render_gui(self, screen, True, True)
        
    def move(self):
        
        for i in self.game.monsters:
            EntityLiving.contact_check(self, i)
           
        EntityLiving.move(self)       