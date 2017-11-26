# -*- coding: utf-8 -*-
import random

import pygame

from Constants import *


class EntityProjectile(pygame.sprite.Sprite):
    
    def __init__(self, game, owner, x, y, speed, damage, direct):
        super(EntityProjectile, self).__init__()
        
        self.game = game
        self.owner = owner
        self.posX = x
        self.posY = y
        self.damage = damage
        self.type = 0
        self.speed = speed
        self.direction = direct
        
        self.image = self.game.assets['ARROW'][self.direction]
        self.rect = self.image.get_rect()        
        self.rect.x = self.posX
        self.rect.y = self.posY
            
    # Движение энтити
    def move(self): 
        if(self.direction == RIGHT): self.rect.x += self.speed
        if(self.direction == DOWN): self.rect.y += self.speed
        if(self.direction == LEFT): self.rect.x -= self.speed
        if(self.direction == UP): self.rect.y -= self.speed
        
        for i in self.game.projectiles:
            if i.rect.x > WIDTH or i.rect.x < -self.rect.size[0] or i.rect.y > HEIGHT or i.rect.y < -self.rect.size[0]:
                self.game.projectiles.remove(self)
  
        for i in self.game.entities:                     
            if pygame.sprite.collide_rect(self, i) and self.owner != i:
                self.set_damage(i)
                
    def set_damage(self, obj):
        obj.hp -= self.damage
        self.remove()
        
    def remove(self):
        self.game.projectiles.remove(self)