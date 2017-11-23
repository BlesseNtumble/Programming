# -*- coding: utf-8 -*-
import random

import pygame

from Constants import *
from entities.base.EntityLiving import EntityLiving


monster_img = ['resources/actor.png', 6, 4, 48] # image, u, v, size

class EntityMonster(EntityLiving):

    def __init__(self, game, position):
        self.game = game
        self.name = 'Enemy'
        self.chars = [100, 100, 0.2, 100] # HP, MP, SPEED, RESPAWN_TIME
        self.based = [self.chars[0], self.chars[1], position[0], position[1], 0.1, 0, self.chars[2]]
        
        self.restime = 0
        EntityLiving.__init__(self, self.game, self.name, self.chars, self.based, DOWN, ALIVE, position, monster_img)

    def render(self, screen):
        EntityLiving.render(self, screen)
        EntityLiving.render_gui(self, screen, True, False)
        
    def tick(self):        
        
        EntityLiving.tick(self)       

        # Воскрешение
        if self.tick_living % 10 == 0 and self.animation == DEAD:
            self.restime += 1
            if(self.restime >= self.chars[3]): 
                self.ressurection()
                
            if self.game.isDebug: 
                print("Entity: %s | PosX: %s | PosY: %s | RespTime: %s" % (self.name, self.posX, self.posY, self.restime))
        
        # Test AI
        if self.animation != DEAD and self.tick_living % 40 == 0:
            j = random.randint(0, 10)
            
            if j == 0: self.movedir = [1, 0, 0, 0]
            if j == 1: self.movedir = [0, 1, 0, 0]
            if j == 2: self.movedir = [0, 0, 1, 0]
            if j == 3: self.movedir = [0, 0, 0, 1]
            if j >= 4: 
                self.movedir = [0, 0, 0, 0]
                self.animation = 1
          
    def ressurection(self):
        self.hp = self.based[0]
        self.mp = self.based[1]
        self.animation = ALIVE
        self.posX = self.start_parameters[2]
        self.posY = self.start_parameters[3]
        self.restime = 0
        
    