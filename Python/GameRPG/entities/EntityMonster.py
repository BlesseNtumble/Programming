# -*- coding: utf-8 -*-
import random

import pygame

from Constants import *
from entities.base.EntityLiving import EntityLiving



class EntityMonster(EntityLiving):

    def __init__(self, game, position):
        self.game = game
        self.name = 'Enemy'
        self.chars = [100.0, 100.0, 1.0, 10] # HP, MP, SPEED, RESPAWN_TIME
        self.start_parameters = [self.chars[0], self.chars[1], position[0], position[1], 1.1, 0, self.chars[2]]
        
        self.restime = 0
        EntityLiving.__init__(self, self.game, self.name, self.chars, self.start_parameters, DOWN, ALIVE, position, 'PLAYER')


    def tick(self):        
        EntityLiving.tick(self)

        # Воскрешение
        if self.tick_living % 10 == 0 and self.animation == DEAD:
            self.restime += 1
            if(self.restime >= self.chars[3]): 
                self.ressurection()
                

            print("Entity: %s | PosX: %s | PosY: %s | RespTime: %s" % (self.name, self.rect.x, self.rect.y, self.restime))
        
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
        
            
    def render_ui(self, screen, camera): 
        EntityLiving.render_ui(self, screen, camera, False)

    def ressurection(self):
        self.hp = self.start_parameters[0]
        self.mp = self.start_parameters[1]
        self.animation = ALIVE
        self.rect.x = self.start_parameters[2]
        self.rect.y = self.start_parameters[3] 
        self.speed = self.start_parameters[6]
        self.restime = 0        
    