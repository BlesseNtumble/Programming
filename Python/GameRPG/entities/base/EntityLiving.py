# -*- coding: utf-8 -*-
import math
import random

import pygame

from Constants import *


class EntityLiving(pygame.sprite.Sprite):
    def __init__(self, game, name, chars, base, direct, anim, position, image_id):
        super(EntityLiving, self).__init__()

        self.game = game
        self.animation = anim
        self.direction = direct
        self.name = name
        
        self.level = 1
        self.experience = 0
        
        self.isInBattle = False
        
        self.start_parameters = (base[0], base[1], base[2], base[3], base[4], base[5], base[6]) #HP,MP,X,Y, REGHP, REG,MP, SPEED

        self.skill_list = []
        
        self.hp = float(chars[0])
        self.mp = float(chars[1])
        self.speed = chars[2]
        self.tick_living = 0.0
        
        # Передвижение [D, L, R, U]
        self.movedir = [0, 0, 0, 0]

        self.image_id = image_id
        self.image = self.game.assets[image_id][self.animation][self.direction]
        self.rect = self.image.get_rect()
        
        self.rect.x = position[0]
        self.rect.y = position[1]
        
        self.size = self.rect.size[0]
        
    def tick(self):    
        self.image = self.game.assets[self.image_id][self.animation][self.direction]
        self.tick_living += 1

        if self.hp < 0:
            self.kill()
            
        if self.animation != DEAD:            
            
            if self.movedir[self.direction] == 0 and self.tick_living % 5 == 0:
                self.animation = 1
            
            
            if self.hp < self.start_parameters[0]:
                self.regen('hp', self.start_parameters[4], -1, 10)
                
            if self.mp < self.start_parameters[1]:
                self.regen('mp', self.start_parameters[4], -1, 5)
        
    def set_damage(self, attacker, count):
        if self.hp < count:
            self.kill(attacker)
        else: self.hp -= count
    
    def attack(self):    
        for obj in self.game.entities:
            if self != obj:
                if self.direction == RIGHT:
                    if self.rect.x >= obj.rect.x - obj.size and self.rect.x <= obj.rect.x and  self.rect.y >= obj.rect.y - obj.size and self.rect.y <= obj.rect.y + obj.size:                
                        obj.set_damage(self, 15) 
                 
    def regen(self, typereg, count, time, speedregen):        
        if self.tick_living % speedregen == 0:
            if --time > 0 or time == -1:
                if typereg == 'hp':
                    self.hp += count
                if typereg == 'mp':
                    self.mp += count
                
    # Движение энтити
    def move(self):        

        if self.animation == DEAD: return
        
        t = math.cos(round(self.tick_living))
        
        if(self.movedir[RIGHT]) == 1: 
            self.direction = RIGHT
            self.rect.x += self.speed 
            
        if(self.movedir[LEFT]) == 1: 
            self.direction = LEFT
            self.rect.x -= self.speed
            
        if(self.movedir[DOWN]) == 1: 
            self.direction = DOWN
            self.rect.y += self.speed
            
        if(self.movedir[UP]) == 1:
            self.direction = UP 
            self.rect.y -= self.speed
        
        for i in self.game.entities:
            if i.animation != DEAD:
                if (pygame.sprite.collide_rect(self, i) and self != i) or (i.rect.x > self.game.levels[self.game.current_level].width or i.rect.x < 0 or i.rect.y > self.game.levels[self.game.current_level].height - i.rect.size[0] or i.rect.y < 0):
                    if(self.movedir[RIGHT]) == 1:
                        self.rect.right = i.rect.left
                    if(self.movedir[DOWN]) == 1:
                        self.rect.bottom = i.rect.top
                    if(self.movedir[LEFT]) == 1:
                        self.rect.left = i.rect.right
                    if(self.movedir[UP]) == 1:
                        self.rect.top = i.rect.bottom
            
        
        for i in self.game.blocks:
            if pygame.sprite.collide_rect(self, i) and self != i:
                if(self.movedir[RIGHT]) == 1 and i.block_sides[RIGHT] == 1:
                    self.rect.right = i.rect.left
                if(self.movedir[DOWN]) == 1 and i.block_sides[DOWN] == 1:
                    self.rect.bottom = i.rect.top
                if(self.movedir[LEFT]) == 1 and i.block_sides[LEFT] == 1:
                    self.rect.left = i.rect.right
                if(self.movedir[UP]) == 1 and i.block_sides[UP] == 1:
                    self.rect.top = i.rect.bottom
    
        if(self.movedir[self.direction] != 0):
            if t >= 0:
                self.animation = 0
            elif t <= -0: 
                self.animation = 2
        
    def kill(self, attacker):
        self.hp = 0
        self.speed = 0  
        self.animation = DEAD   
        
        attacker.experience += 50
                     
        print(attacker.experience)
         
    def ressurection(self):
        self.hp = random.randint(int(self.start_parameters[0] / 6), int(self.start_parameters[0] / 2))
        self.mp = random.randint(int(self.start_parameters[1] / 4), int(self.start_parameters[1] / 2))
        self.animation = ALIVE
        self.rect.x = self.start_parameters[2]
        self.rect.y = self.start_parameters[3] 
        self.speed = self.start_parameters[6] 
               
            
    def render_ui(self, screen, camera, window, drawmp):
        if self.animation == DEAD: return
         
        color_font    = (255, 255, 255)      
                    
        fontObj = pygame.font.Font('freesansbold.ttf', 13)
        textSurfaceObj = fontObj.render("[" + str(self.level) + "] " + str(self.name) + " ", False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (camera.apply(self).x + 23, camera.apply(self).y - 25)
        screen.blit(textSurfaceObj, textRectObj)
        
        pygame.draw.rect(screen, (0,0,0), (camera.apply(self).x - 2, camera.apply(self).y - 10 - 6, 52, 5))
        hp = int((self.hp/self.start_parameters[0]) * 50)
        pygame.draw.rect(screen, (220,0,0), (camera.apply(self).x - 1, camera.apply(self).y - 9 - 6, hp, 3))
        
        if drawmp == True:
            pygame.draw.rect(screen, (0,0,0), (camera.apply(self).x - 2, camera.apply(self).y - 10, 52, 5))        
            mp = int((self.mp/self.start_parameters[1]) * 50)
            pygame.draw.rect(screen, (0,220,220), (camera.apply(self).x - 1, camera.apply(self).y - 9, mp, 3))
        
    def useSkill(self, skillid):        
        self.skill_list[skillid].useSkill()
        
    def find_target(self, target):
        return ((target.rect.x) // 48, (target.rect.y) // 48)
    
    def find_self(self):
        return self.find_target(self)
    
    def change_move(self, direction):
        if self.animation != DEAD:
            self.movedir = [0, 0, 0, 0]
            self.direction = direction
            if 0 <= direction <= 3:
                self.movedir[direction] = 1