# -*- coding: utf-8 -*-
import pygame
from Constants import *


class EntityProjectile():
    
    def __init__(self, game, x, y, speed, damage, direct, image_pack):
        self.game = game
        self.posX = x
        self.posY = y
        self.damage = damage
        self.type = 0
        self.speed = speed
        self.direction = direct
        self.image = image_pack[0]
        self.u = image_pack[1]
        self.v = image_pack[2]
        self.size = image_pack[3]
        self.images = []
        
        temp = pygame.image.load(self.image).convert_alpha()
        
        for m in range(self.u):
            i = []
            for k in range(self.v):                                      
                i.append(temp.subsurface(self.size * m, self.size * k, self.size, self.size))
            self.images.append(i)
            
    # Движение энтити
    def move(self): 
        if(self.direction == RIGHT): self.posX += self.speed
        if(self.direction == DOWN): self.posY += self.speed
        if(self.direction == LEFT): self.posX -= self.speed
        if(self.direction == UP): self.posY -= self.speed
        for i in self.game.monsters:
            self.hit_check(i)
        
    def hit_check(self, obj):
        if self.direction == RIGHT:
            if self.posX >= obj.posX - obj.size + 15 and self.posY >= obj.posY - obj.size + 25 and self.posY <= obj.posY + obj.size :                
                self.set_damage(obj)
       
    def set_damage(self, obj):
        obj.hp -= self.damage
        self.remove()
        
    def remove_projetile(self):
        for i in self.game.projectiles:
            if i.posX > WIN_WIDTH or i.posX < -self.size or i.posY > WIN_HEIGHT or i.posY < -self.size:
                self.game.projectiles.remove(i)
         
    
    def render(self, screen):       
        screen.blit(self.images[self.type][self.direction], (self.posX, self.posY))
        
    def remove(self):
        self.game.projectiles.remove(self)