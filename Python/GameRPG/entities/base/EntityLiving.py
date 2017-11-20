# -*- coding: utf-8 -*-
import math
import random

import pygame

from Constants import *


class EntityLiving():
    def __init__(self, game, name, chars, base, direct, anim, position, image_list):
        self.game = game
        self.animation = anim
        self.direction = direct
        self.posX = position[0]
        self.posY = position[1]
        self.name = name
        
        self.start_parameters = (base[0], base[1], base[2], base[3])
        
        self.hp = chars[0]
        self.mp = chars[1]
        self.speed = chars[2]
        self.tick_living = 0.0
        
         # Передвижение [D, L, R, U]
        self.movedir = [0, 0, 0, 0]
        self.blocked = [0, 0, 0, 0]
        self.size = image_list[3]
        self.image_list = image_list[0]
        self.u = image_list[1]
        self.v = image_list[2]
        self.images = []
        
        temp = pygame.image.load(self.image_list).convert_alpha()           

        for m in range(self.u):
            i = []
            for k in range(self.v):                                      
                i.append(temp.subsurface(self.size * m, self.size * k, self.size, self.size))
            self.images.append(i)
                
    def tick(self):
        if self.animation != DEAD:
            if self.hp > 0 and self.hp < 100:
                self.hp += HP_REG            
            if self.mp < 100:
                self.mp += MP_REG
                
            if self.hp <= 0:
                self.kill()
        
        self.tick_living += 1

    def kill(self):
        self.hp = 0
        self.mp = 0
        self.animation = DEAD
        
    def ressurection(self):
        self.hp = random.randint(int(self.start_parameters[0] / 6), int(self.start_parameters[0] / 2))
        self.mp = random.randint(int(self.start_parameters[1] / 4), int(self.start_parameters[1] / 2))
        self.animation = ALIVE
        self.posX = self.start_parameters[2]
        self.posY = self.start_parameters[3]
        
    # Движение энтити
    def move(self):        

        if self.animation == DEAD: return
        
        t = math.cos(round(self.tick_living))
        self.block_check()
        
        if(self.movedir[RIGHT]) == 1: 
            self.direction = RIGHT
            if self.blocked[RIGHT] == 0: self.posX += self.speed            
            
        if(self.movedir[LEFT]) == 1: 
            self.direction = LEFT
            if self.blocked[LEFT] == 0: self.posX -= self.speed
            
        if(self.movedir[DOWN]) == 1: 
            self.direction = DOWN
            if self.blocked[DOWN] == 0: self.posY += self.speed
            
        if(self.movedir[UP]) == 1:
            self.direction = UP 
            if self.blocked[UP] == 0: self.posY -= self.speed
        
        if(self.movedir[UP] != 0 or self.movedir[DOWN] != 0 or self.movedir[LEFT] != 0 or self.movedir[RIGHT] != 0):
            if t >= 0: self.animation = 0
            elif t <= -0: self.animation = 2
            
    def block_check(self):         
        
        if (self.animation == DEAD): self.blocked = [1, 1, 1, 1]
        # Блокировка выхода за экран
        # [0, 0]
        if self.posX <= 0: self.blocked[LEFT] = 1
        if self.posY <= 0: self.blocked[UP] = 1
        # [N, M]
        if self.posX >= WIN_WIDTH - self.size: self.blocked[RIGHT] = 1
        if self.posY >= WIN_HEIGHT - self.size: self.blocked[DOWN] = 1
        
    def contact_check(self, obj):
               
        x1 = self.posX
        y1 = self.posY
        x2 = obj.posX
        y2 = obj.posY
        
        if obj.animation == DEAD: return
        
        #RIGHT
        elif x1 >= x2 - obj.size and y1 <= y2 + obj.size - 15 and y1 >= y2 - obj.size + 15 and x1 <= x2 + obj.size - 15:
            self.blocked = [0, 0, 1, 0]       
        #LEFT
        elif x1 <= x2 + obj.size - 5 and x1 >= x2 + obj.size - 15 and y1 <= y2 + obj.size - 15 and y1 >= y2 - obj.size + 15: 
            self.blocked = [0, 1, 0, 0]              
        #DOWN
        elif y1 <= y2 + obj.size - 20 and y1 >= y2 - obj.size and x1 >= x2 - obj.size + 15 and x1 <= x2 + obj.size - 15:  
            self.blocked = [1, 0, 0, 0]            
        #UP 
        elif y1 <= y2 + obj.size - 14 and y1 >= y2 - obj.size and x1 >= x2 - obj.size + 15 and x1 <= x2 + obj.size - 15:
            self.blocked = [0, 0, 0, 1]
        #UNBLOCK            
        else: self.blocked = [0, 0, 0, 0]  
        
        
    # Отрисовка энтити
    def render(self, screen):
        screen.blit(self.images[self.animation][self.direction], (self.posX, self.posY))
    
    # Отрисовка графического интерфейса
    def render_gui(self, screen, hp, mp):
        
        if self.animation == DEAD: return
        
        color_font    = (255, 255, 255)      
        color_bg      = (30, 30, 30)
             
        fontObj = pygame.font.Font('freesansbold.ttf', 13)
        textSurfaceObj = fontObj.render(" " + str(self.name) + " ", False, color_font, color_bg)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (self.posX + 23, self.posY - 25)

        screen.blit(textSurfaceObj, textRectObj)
        
        if hp == True: 
            screen.blit(pygame.image.load('resources/bar.png'), (self.posX - 3, self.posY - 15))
        
            m = 1
            z = self.hp // 4        
            while m <= z:
                screen.blit(pygame.image.load('resources/hp.png'), (self.posX - 4 +m*2, self.posY - 14))
                m += 1
        
        if mp == True: 
            screen.blit(pygame.image.load('resources/bar.png'), (self.posX - 3, self.posY - 9))
          
            v = 1  
            n = self.mp // 4
            while v <= n:
                screen.blit(pygame.image.load('resources/mp.png'), (self.posX - 4 +v*2, self.posY - 8))
                v += 1
      
    