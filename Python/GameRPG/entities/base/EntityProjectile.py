# -*- coding: utf-8 -*-
import random

import pygame

from Constants import *


class EntityProjectile(pygame.sprite.Sprite):
    
    def __init__(self, game, owner, image, x, y, speed, damage, distance, direct):
        super(EntityProjectile, self).__init__()
        
        self.game = game
        self.owner = owner

        self.damage = damage
        self.type = 0
        self.speed = speed
        self.distance = distance
        self.direction = direct
        
        self.image = image
        self.rect = self.image.get_rect()        
        self.rect.x = x
        self.rect.y = y
        
    # Движение энтити
    def move(self): 
        l_x = self.owner.rect.x
        l_y = self.owner.rect.y
        
        if(self.direction == RIGHT): self.rect.x += self.speed
        if(self.direction == DOWN): self.rect.y += self.speed
        if(self.direction == LEFT): self.rect.x -= self.speed
        if(self.direction == UP): self.rect.y -= self.speed
        
        for i in self.game.projectiles:
            if i.rect.x > self.game.levels[self.game.current_level].width  or i.rect.x < -self.rect.size[0] or i.rect.y > self.game.levels[self.game.current_level].height or i.rect.y < -self.rect.size[0]:
                self.remove()
            if self.distance > 0:
                if i.rect.x > l_x + self.distance or i.rect.x < l_x - 250 or i.rect.y > l_y + self.distance or i.rect.y < l_y - self.distance:
                    self.remove()
            
            
        for i in self.game.entities:                     
            if pygame.sprite.collide_rect(self, i) and self.owner != i:
                self.set_damage(i)
                
    def set_damage(self, obj):
        obj.set_damage(self.damage)
        self.remove()
        
    def remove(self):
        self.game.projectiles.remove(self)