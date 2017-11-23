# -*- coding: utf-8 -*-
from Constants import *
from entities.base.EntityLiving import *
from skills.Skills import Skills, Arrow


position = [150, 50]
char_img = ['resources/actor.png', 6, 4, 48] # image, u (width), v (height), size

class EntityPlayer(EntityLiving):
    
    def __init__(self, game):
        self.name = 'Little Boy'
        self.game = game
        self.chars = [100, 100, SPEED] #HP, MP, SPEED
        self.base = [self.chars[0], self.chars[1], position[0], position[1], HP_REG, MP_REG, SPEED]       
        EntityLiving.__init__(self, self.game, self.name, self.chars, self.base, DOWN, ALIVE, position, char_img)    
    
        self.skill_list.append(Arrow(self))
    
    def useSkill(self):        
        self.skill_list[0].useSkill()
        
    def tick(self):
        EntityLiving.tick(self)
        for i in self.skill_list:
            i.tick()
            
    def render(self, screen):
        EntityLiving.render(self, screen)
        EntityLiving.render_gui(self, screen, True, True)
        
    def block_check(self):         
        
        self.blocked = [0, 0, 0, 0] 
        
        for i in self.game.blocks:
            if i.block_sides[self.direction] != 0: self.contact_check(i)   
        for i in self.game.monsters:
            if i != self: self.contact_check(i)
            
        if (self.animation == DEAD): self.blocked = [1, 1, 1, 1]
        # Блокировка выхода за экран
        # [0, 0]
        if self.posX <= 0: self.blocked[LEFT] = 1
        if self.posY <= 0: self.blocked[UP] = 1
        # [N, M]
        if self.posX >= WIN_WIDTH - self.size: self.blocked[RIGHT] = 1
        if self.posY >= WIN_HEIGHT - self.size: self.blocked[DOWN] = 1