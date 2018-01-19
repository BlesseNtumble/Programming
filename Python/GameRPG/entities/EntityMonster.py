# -*- coding: utf-8 -*-
import random

import pygame

from Constants import *
from entities.base.EntityLiving import EntityLiving
from skills.Skills import Arrow

class EntityMonster(EntityLiving):

    def __init__(self, game, position, level):
        self.game = game
        self.name = 'Enemy ' + str(random.randint(0, 3))
        self.chars = [100.0, 100.0, 1, 10] # HP, MP, SPEED, RESPAWN_TIME
        self.start_parameters = [self.chars[0], self.chars[1], position[0], position[1], 1.1, 0, self.chars[2]]
               
        self.restime = 0
        EntityLiving.__init__(self, self.game, self.name, self.start_parameters, DOWN, ALIVE, position, 'PLAYER')

        self.level = level
        self.target = self.game.player
        #self.last_coords = self.find_target(self.target)
        #self.path = self.path_find(self.last_coords)
        
       
        self.skill_list.append(Arrow(self, 0, 4))  
        
        self.xsize = 32
        self.ysize = 48
        
        self.type = AGRESSIVE
        self.attack_type = MELEE
        
        self.start_parameters[0] = self.hp = HP[self.level - 1] / 2
        self.start_parameters[1] = self.mp = MP[self.level - 1] / 2
                    
    def tick(self): 
        
        EntityLiving.tick(self)

        # Воскрешение
        if self.tick_living % 10 == 0 and self.animation == DEAD:
            self.restime += 1
            if(self.restime >= self.chars[3]): 
                self.ressurection()
            print("Entity: %s | PosX: %s | PosY: %s | RespTime: %s" % (self.name, self.rect.x, self.rect.y, self.restime))
    
        radius = 200
          
        if self.type != PASSIVE:      
            self.target = self.getEntityInRange(self, radius, self.game.player)
        
        #if (self.target != None): print(self.getEntityInFace(self, self.target))

        if self.tick_living % 4 == 0 and self.animation != DEAD:               
            
            if self.type == AGRESSIVE and self.target != None and self.target.animation != DEAD:
                
                if self.target == self.game.player:
                    if self.attack_type == MELEE:
                        if(self.rect.y + self.xsize/2 > self.target.rect.y) and (self.rect.y - self.ysize/2 < self.target.rect.y):
                           
                            if(self.rect.x + self.xsize/2 < self.target.rect.x): self.change_move(RIGHT)
                            elif(self.rect.x > self.target.rect.x): self.change_move(LEFT)
                        elif(self.rect.y + self.ysize/2 + 1> self.target.rect.y): self.change_move(UP)
                        elif(self.rect.y - self.ysize/2 - 1< self.target.rect.y): self.change_move(DOWN)
    
                        if self.getEntityInFace(self, self.target):
                            self.attack(3, 4 * self.level)
                    elif self.attack_type == RANGE:
                        pass
            else:
                
                j = random.randint(0, 50)
            
                if j == 0: self.change_move(DOWN)
                if j == 1: self.change_move(LEFT)
                if j == 2: self.change_move(RIGHT)
                if j == 3: self.change_move(UP)
                if j >= 4:  
                    self.movedir = [0, 0, 0, 0]
                    self.animation = 1            

        
    def move(self):
        if(self.movedir[self.direction] == 1 and self.getBlocksInRange(self, self.xsize, self.ysize, True)):
            if(self.movedir[RIGHT]) == 1:
                    self.rect.x -= self.speed            
            if(self.movedir[LEFT]) == 1:
                    self.rect.x += self.speed
            if(self.movedir[DOWN]) == 1:
                    self.rect.y -= self.speed
            if(self.movedir[UP]) == 1:
                    self.rect.y += self.speed
            self.movedir[self.direction] = 0
            
        return EntityLiving.move(self)
    
    def render_ui(self, screen, camera, window):                 
        EntityLiving.render_ui(self, screen, camera, window, False)
        color_font  = (255, 255, 255)
        
        
        textSurfaceObj = self.font.render('Target: ' + str(self.target), False, color_font)       
        screen.blit(textSurfaceObj, (camera.apply(self).x - 20, camera.apply(self).y + 70))

        if(self.game.player.level - self.level > 3): color_font = (0, 0, 255)
        elif(self.game.player.level - self.level == 3): color_font = (0, 255, 0)
        elif(self.game.player.level - self.level == 2): color_font = (255, 255, 255)
        elif(self.game.player.level - self.level == -2): color_font = (255, 255, 0)
        elif(self.game.player.level - self.level == -3): color_font = (205, 80, 40)
        elif(self.game.player.level - self.level < -3): color_font = (255, 0, 0)
        textSurfaceObj = self.font.render(str(self.level) + " " + str(self.name) + " ", False, color_font)       
        screen.blit(textSurfaceObj, (camera.apply(self).x - len(self.name) + 3, camera.apply(self).y - 35))
     
    def ressurection(self):
        self.hp = self.start_parameters[0]
        self.mp = self.start_parameters[1]
        self.animation = ALIVE
        self.rect.x = self.start_parameters[2]
        self.rect.y = self.start_parameters[3] 
        self.speed = self.start_parameters[6]
        self.restime = 0        
    """
    #Метод Дейкстры
    def path_find(self, target):
        lvl = self.game.levels[self.game.current_level].ai_level()
        
        coords = self.find_self()
        mark = ways = lvl.copy()
        for i in mark:
            mark[i] = False
        for i in ways:
            ways[i] = None
            
        mark[coords] = True
        ways[coords] = list()
        ways[coords].append(coords)
        while ways[target] == None:
            for i in lvl:
                if mark[i] == True:
                    for x in lvl[i]:
                        if ways[x] == None:
                            z = ways[i].copy()
                            z.append(x)
                            ways[x] = z
            for i in lvl:
                if ways[i] != None: mark[i] = True
                
        return ways[target]
    
    def choose_move(self):
        coords = self.find_self()
        
        if(self.last_coords != self.find_target(self.game.player)):
            self.path = self.path_find(self.find_target(self.game.player))
        
        if(self.movedir[LEFT] == 1):
            coords = ((self.rect.x + self.size) // 64, self.rect.y // 64)
        if(self.movedir[UP] == 1):
            coords = (self.rect.x // 64, (self.rect.y + self.size) // 64)
            
        if coords == self.path[0]:
            self.path.pop(0)
            
        if len(self.path) == 0:
            self.speed = 0
        elif self.path[0][0] > coords[0]:
            self.change_move(RIGHT)
        elif self.path[0][0] < coords[0]:
            self.change_move(LEFT)
        elif self.path[0][1] > coords[1]:
            self.change_move(DOWN)
        elif self.path[0][0] < coords[1]:
            self.change_move(UP)
    
    def cast_check(self):
        if self.direction == RIGHT or self.direction == LEFT:
            if(self.target.rect.y < self.rect.y + self.size/2 and self.target.rect.y > self.rect.y - self.size/2):
                self.useSkill(0)
        if self.direction == DOWN or self.direction == UP:
            if(self.target.rect.x < self.rect.x + self.size/2 and self.target.rect.x > self.rect.x - self.size/2):
                self.useSkill(0)
    """