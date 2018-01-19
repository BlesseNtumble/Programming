# -*- coding: utf-8 -*-
import math
import random

import pygame

from Constants import *

class EntityLiving(pygame.sprite.Sprite):
       
    def __init__(self, game, name, base, direct, anim, position, image_id):
        super(EntityLiving, self).__init__()

        self.game = game
        self.animation = anim
        self.direction = direct
        self.name = name
        
        self.level = 1
        self.experience = 0
        
        self.isInBattle = False
        
        self.start_parameters = [base[0], base[1], base[2], base[3], base[4], base[5], base[6]] #HP,MP,X,Y, REGHP, REG,MP, SPEED

        self.skill_list = []
        
        self.hp = HP[self.level - 1]
        self.mp = self.start_parameters[1]
        
        self.speed = float(self.start_parameters[6])
        self.tick_living = 0.0
        
        # Передвижение [D, L, R, U]
        self.movedir = [0, 0, 0, 0]

        self.image_id = image_id
        self.image = self.game.assets[image_id][self.animation][self.direction]
        self.rect = self.image.get_rect()
        
        self.rect.x = position[0]
        self.rect.y = position[1]
        
        self.xsize = self.rect.size[0]
        self.ysize = self.rect.size[1]
        
        self.font = pygame.font.Font('freesansbold.ttf', 13)
        self.attack_cooldown = 0  
        
        self.damage_count = 0 
        self.damage_y = 0
        
    def tick(self):    
        self.image = self.game.assets[self.image_id][self.animation][self.direction]
        self.tick_living += 1

        if self.isInBattle == True: 
            if self.tick_living % 15 == 0:
                self.isInBattle = False
                self.damage_y = 0
            
        [i.tick() for i in self.skill_list]   
        
        if self.hp <= 0:
            self.kill()           
        
        if self.animation != DEAD:                    
            if self.movedir[self.direction] == 0 and self.tick_living % 5 == 0 and self.isInBattle == False:
                self.animation = 1   
                             
            if self.attack_cooldown > 0 and self.tick_living % 5 == 0:
                self.attack_cooldown -= 1
                
            if(self.movedir[self.direction] != 0):
                t = math.cos(int(self.tick_living * 1.5))
                print(t)
                if t >= 0:
                    self.animation = 0
                elif t < 0: 
                    self.animation = 2
            
            if self.isInBattle == False and self.tick_living % 10 == 0:
                self.regen('hp', 1)
                self.regen('mp', 2)
                
                        
    def set_damage(self, attacker, count):
        if self.hp < count:
            self.kill(attacker)
        else: self.hp -= count 

        self.isInBattle = True
        self.damage_count = count
        
    def attack(self, cooldown, count):
        print(self.getEntityInFace(self))
        if(self.attack_cooldown == 0):
            if self.getEntityInFace(self) != None:
                self.getEntityInFace(self).set_damage(self, count)
            self.animation = 5
            self.attack_cooldown = cooldown
                 
    def regen(self, typereg, count): 
        if typereg == 'hp' and self.hp < self.start_parameters[0]:
            if(self.hp + count > HP[self.level - 1]): self.hp += HP[self.level - 1] - self.hp
            else: self.hp += count
        if typereg == 'mp' and self.mp < self.start_parameters[1]:
            if(self.mp + count > MP[self.level - 1]): self.mp += MP[self.level - 1] - self.mp           
            else: self.mp += count
               
    def getEntityInRange(self, obj, radius, target=None):
        for i in self.game.entities: 
            if(obj != i) and i.animation != DEAD and self.animation != DEAD:
                if(i.rect.x > obj.rect.x - radius) and (i.rect.x < obj.rect.x + radius) and (i.rect.y > obj.rect.y - radius) and (i.rect.y < obj.rect.y + radius):
                    if(target != None):
                        if i == target:
                            return i
                    else: return i
                
    def getBlocksInRange(self, obj, radiusx, radiusy, checkblocks):
        for i in self.game.blocks: 
            if self.animation != DEAD and i.block_sides[self.direction] == 1:
                if(i.rect.x > obj.rect.x - radiusx) and (i.rect.x < obj.rect.x + radiusx) and (i.rect.y > obj.rect.y - radiusy) and (i.rect.y < obj.rect.y + radiusy):
                    return i
                   
    def getEntityInFace(self, obj, target=None):
        for i in self.game.entities:
            if(obj != i) and i.animation != DEAD and obj.animation != DEAD:
                if obj.direction == RIGHT:
                    if(i.rect.x > obj.rect.x + obj.xsize/2 - 5) and (i.rect.x < obj.rect.x + obj.xsize + 5) and (i.rect.y > obj.rect.y - obj.ysize/2 - 5) and (i.rect.y < obj.rect.y + obj.ysize/2):
                        if target != None:
                            if i == target:
                                return i
                        else: return i 
                if obj.direction == LEFT:
                    if(i.rect.x > obj.rect.x - obj.xsize - 5) and (i.rect.x < obj.rect.x - obj.xsize/2 + 5) and (i.rect.y > obj.rect.y - obj.ysize/2 - 5) and (i.rect.y < obj.rect.y + obj.ysize/2):
                        if target != None:
                            if i == target:
                                return i
                        else: return i 
                if obj.direction == UP:
                    if(i.rect.x > obj.rect.x - obj.xsize/2 - 20) and (i.rect.x < obj.rect.x + obj.xsize/2 + 20) and (i.rect.y > obj.rect.y - obj.ysize - 1) and (i.rect.y < obj.rect.y + obj.ysize/2):
                        if target != None:
                            if i == target:
                                return i
                        else: return i 
                if obj.direction == DOWN:
                    if(i.rect.x > obj.rect.x - obj.xsize/2 - 20) and (i.rect.x < obj.rect.x + obj.xsize/2 + 20) and (i.rect.y > obj.rect.y - obj.ysize/2) and (i.rect.y < obj.rect.y + obj.ysize + 1):
                        if target != None:
                            if i == target:
                                return i
                        else: return i                 
   
    # Движение энтити
    def move(self):        

        if self.animation == DEAD: return
        
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
                if (pygame.sprite.collide_rect(self, i) and self != i):
                    
                    if(self.movedir[RIGHT]) == 1:
                        self.rect.right = i.rect.left
                    if(self.movedir[DOWN]) == 1:
                        self.rect.bottom = i.rect.top
                    if(self.movedir[LEFT]) == 1:
                        self.rect.left = i.rect.right
                    if(self.movedir[UP]) == 1:
                        self.rect.top = i.rect.bottom         
                    self.movedir[self.direction] = 0
                    
    def kill(self, attacker=None):
        self.hp = 0
        self.speed = 0.0
        self.animation = DEAD   
        
        if(attacker != None):
            attacker.experience += 50 * self.level                     
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
       
        textSurfaceObj = self.font.render("-" + str(int(self.damage_count)), False, color_font) 
        
        if self.isInBattle:
            self.damage_y += 1                   
            self.game.screen.blit(textSurfaceObj, (self.game.camera.apply(self).x + 60, self.game.camera.apply(self).y - 15 - self.damage_y)) 
    
        textSurfaceObj = self.font.render("X: " + str(self.rect.x) + " | Y: " + str(self.rect.y), False, color_font)       
        screen.blit(textSurfaceObj, (camera.apply(self).x - 20, camera.apply(self).y + 55))
          
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