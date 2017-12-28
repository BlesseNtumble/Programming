from pygame import *
import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, uv, image_id, block_sides, layer=None, blockprojectile=None):
        pygame.sprite.Sprite.__init__(self)
        
        self.game = game
        
        self.image_id = image_id
        self.block_sides = block_sides
        self.image = self.game.assets[self.image_id][uv[0]][uv[1]]
        
        self.rect = self.image.get_rect()        
        self.rect.x = x
        self.rect.y = y       
        self.size = self.rect.size[0]  
        
        self.block_proj = blockprojectile  
        self.layer = layer
        
    def tick(self):
        pass       

    
class Blocks(Block):
    def __init__(self, game, pos, uv, name, blocked, layer=None):
        Block.__init__(self, game, pos[0], pos[1], uv, name, blocked, layer)
        
class ChangeLevelBlock(Block):
    def __init__(self, game, pos, uv, blocked, level, x=None, y=None):
        self.level = level
        self.playerX = x
        self.playerY = y
        Block.__init__(self, game, pos[0], pos[1], uv, 'GRASS', blocked)
    
    def tick(self):
        if(self.game.player.rect.x >= self.rect.x - 20 and self.game.player.rect.x <= self.rect.x + 20 and self.game.player.rect.y >= self.rect.y - 40 and self.game.player.rect.y <= self.rect.y):
            
            self.game.gen_world(self.level)
            
            if (self.playerX != None):
                self.game.player.rect.x = self.playerX 
            if (self.playerY != None):       
                self.game.player.rect.y = self.playerY       
            print(self.game.player.rect.x, self.rect.x)