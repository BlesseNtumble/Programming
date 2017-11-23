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

        self.isInBattle = False
        
        self.start_parameters = (base[0], base[1], base[2], base[3], base[4], base[5], base[6]) #HP,MP,X,Y, REGHP, REG,MP, SPEED

        self.skill_list = []
        
        self.hp = float(chars[0])
        self.mp = float(chars[1])
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
        
        if self.hp <= 0:
            self.kill()
        
        if self.animation != DEAD:
            if self.hp > 0 and self.hp < self.start_parameters[0]:
                self.hp += float(self.start_parameters[4])        
            if self.mp < 100:
                self.mp += float(self.start_parameters[5])
                
            if self.speed <= 0 and self.isInBattle == False:
                self.speed = 0
                self.animation = 1
                
            if self.movedir[self.direction] == 0:
                self.speed = 0  
            else: self.speed = self.start_parameters[6] 
            
            if self.tick_living % 3 == 0:                
                if self.animation == 4:
                    self.animation = 5
                    
                elif self.animation == 5:
                    self.animation = 1
                    
            if self.tick_living % 8 == 0:
                if self.isInBattle == True:
                    self.isInBattle = False
                
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
        
    def attack(self):
        self.animation = 4        
        for i in self.game.monsters:
            self.hit_check(i)
              
    def hit_check(self, obj):
        self.isInBattle = True
        if self.direction == RIGHT:
            if self.posX >= obj.posX - obj.size + 10 and self.posX <= obj.posX and  self.posY >= obj.posY - obj.size + 20 and self.posY <= obj.posY + obj.size - 25:                
                obj.hp -= 15  
        if self.direction == LEFT:
            if self.posX >= obj.posX - obj.size and self.posX <= obj.posX + obj.size - 10 and self.posY >= obj.posY - obj.size - 15 and self.posY <= obj.posY + obj.size - 25:                
                obj.hp -= 15
                
         
    # Движение энтити
    def move(self):        

        if self.animation == DEAD: return
        
        self.blocked = [0, 0, 0, 0] 
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
        
        if self.isInBattle == False:
            if(self.movedir[UP] != 0 or self.movedir[DOWN] != 0 or self.movedir[LEFT] != 0 or self.movedir[RIGHT] != 0):
                if t >= 0:
                    self.animation = 0
                elif t <= -0: 
                    self.animation = 2
            
    def block_check(self):         
        
        for i in self.game.blocks:
            if i.block_sides[self.direction] != 0: self.contact_check(i)            
            
        for i in self.game.monsters:
            if i != self: self.contact_check(i)
            
        self.contact_check(self.game.player)
            
        if (self.animation == DEAD): self.blocked = [1, 1, 1, 1]
        # Блокировка выхода за экран
        # [0, 0]
        if self.posX <= 0: self.blocked[LEFT] = 1
        if self.posY <= 0: self.blocked[UP] = 1
        # [N, M]
        if self.posX >= WIN_WIDTH - self.size: self.blocked[RIGHT] = 1
        if self.posY >= WIN_HEIGHT - self.size: self.blocked[DOWN] = 1
        

    def contact_check(self, obj):
       
        #TODO ДОРАБОТАТЬ СРОЧНА!!!!!!!!!!!
        #КРИВОЙ ГОВНОСКРИПТ!!!
        par1 = 10
        
        #RIGHT
        if self.posX >= obj.posX - obj.size + par1 and self.posX <= obj.posX + obj.size - par1 and self.posY >= obj.posY - obj.size + par1 - 5 and self.posY <= obj.posY + obj.size - par1:
            self.blocked = [0, 0, 1, 0]        
        #LEFT        
        if self.posX <= obj.posX + obj.size - par1 and self.posX >= obj.posX + obj.size - par1 and self.posY >= obj.posY - obj.size + par1 - 5 and self.posY <= obj.posY + obj.size - par1: 
            self.blocked = [0, 1, 0, 0]
        """
        #DOWN
        if self.posY <= obj.posY + obj.size and self.posY >= obj.posY - obj.size + 15 and self.posX >= obj.posX - obj.size + par1 and self.posX <= obj.posX + obj.size - par1:  
            self.blocked = [1, 0, 0, 0] 
        
        #UP 
        if self.posY <= obj.posY + obj.size - 25 and self.posY >= obj.posY - obj.size - 5 and self.posX >= obj.posX - obj.size and self.posX <= obj.posX + obj.size:
            self.blocked = [0, 0, 0, 1]
        """
        
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
      
    